from asyncio.log import logger
from audioop import reverse
import json
import operator
from unittest import result
from urllib import response
from collections import OrderedDict
from flask import jsonify, session, request
from  flask_restful import Api, Resource
from api.models.users import User
from api.schemas.users import UserSchema
from api.settings.base import Session


from sa_filters import apply_pagination, apply_filters

import logging
import config

logger = logging.getLogger(__name__)

class ApiInit(Resource):
    def get(self):
        return {
            'success': True
        }

class Utils():
    def api_resources(self, param, opt):
        session = Session()
        response = []
        if param == 'search':
            for values in range(len(opt)):
                user = []
                for key in opt[values]:
                    if key == "name":
                        user = session.query(User).filter(User.name.ilike(opt[values][key]))
                    if key == "lastname":
                        user = session.query(User).filter(User.lastname.ilike(opt[values][key]))
                [response.append(user_listed) for user_listed in user]
        return response

    def response_formatter(self, resource, ordering):
        users_schema = UserSchema(many=True)
        results = users_schema.dump(resource) if len(resource) > 0 else {}
        if len(resource) > 0 : results= sorted(results, key=operator.itemgetter('name'), reverse=ordering)
        return results


class UsersResource(Resource):
    def get(self, page_size=None):
        """
        Retreive user data from database source
        ---
        parameters:
          - in: query
            name: page_size
            type: number
          - in: query
            name: page_number
            type: number
          - in: query
            name: sort
            type: string
            enum: [asc, desc]
          - in: body
            schema:
                type: object
                required:
                - userName
                properties:
                name:
                    type: string
                lastName:
                    type: string
        responses:
          200:
            description: Retrieve user data
            schema:
              id: User
              properties:
                name:
                  type: string
                  description: The name of the user
                lastname:
                  type: string
                  description: The name of the user
          201:
            description: Retrieve user data by pagination results
            content:
                application/json:
                    schema:
                        id: User
                        properties:
                            success: 
                               type:boolean
                            page: 
                               type:integer
                            chunk: 
                               type:integer
                            results:
                               type: object
                               properties:
                                    name: 
                                        type:string
                                    lastname:
                                        type:string
                            total_pages:
                               type:integer
                            count: 
                               type:integer
        """
        utils = Utils()
        page_size = config.ApiSetting.PAGESIZE
        page_number = config.ApiSetting.PAGENUMBER
        sort_default = config.ApiSetting.SORT
        try:
            """
            ARGS validation
            """
            pagination_arg = "page_size"
            page_arg = "page_number"
            sorting_arg = "sort"
            filter_arg = "search"
            data_arg = request.get_json() if request.data else None
            sort_arg = request.args.get(sorting_arg)

            if sort_arg != None and  sort_arg != 'asc' : sort_default =  True
            logger.info(f"Setting filtering query")

            if data_arg != None:
                resource = utils.api_resources(filter_arg, data_arg)
                results = utils.response_formatter(resource, sort_default)
                logger.info(f"Formatting response resource")
                
                response = {
                'success': True,
                'results' : results
            }
            else:
                results = User.query
                page_size_arg = request.args.get(pagination_arg)
                page_number_arg = request.args.get(page_arg)
                logger.info(f"Setting pagination parameters")
                if page_size_arg != None : page_size =  int(page_size_arg)
                if page_number_arg != None : page_number =  int(page_number_arg)
                page, pagination = apply_pagination(results, page_number=page_number, page_size=page_size)
                page_size, page_number, num_pages, total_results = pagination
                resource = page.all()
                logger.info(f"Formatting response resource")
                results = utils.response_formatter(resource, sort_default)
                response ={
                'success': True,
                'page':page_size,
                'chunk':page_number,
                'results' : results,
                'total_pages': num_pages,
                'count': total_results
            }

            return response, 200

        except ValueError as e:
            print('%s', e)

        except NameError as e:
            print("-----",e)