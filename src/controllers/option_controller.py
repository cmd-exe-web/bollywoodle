from flask_restful import Resource, reqparse
from ..services.option_service import OptionService

parser = reqparse.RequestParser()
parser.add_argument('name', action='append',
                    required=True, help='Name is required')


class OptionListResource(Resource):
    def get(self):
        options = OptionService.get_all_options()
        return [{'id': str(option.id), 'name': option.name} for option in options]

    def post(self):
        data = parser.parse_args()
        list = data['name']

        if list:
            created_options = []
            for name in list:
                try:
                    new_option = OptionService.create_option(name)
                    created_options.append(
                        {'id': str(new_option.id), 'name': new_option.name})
                except Exception as e:
                    return str(e), 409

            return created_options, 201
        else:
            return {'message': "Invalid format: No 'name' field found"}, 400


class OptionResource(Resource):
    def get(self, option_id):
        option = OptionService.get_option_by_id(option_id)
        if option:
            return {'id': str(option.id), 'name': option.name}
        return {'message': "Option not found"}, 404

    def put(self, option_id):
        args = parser.parse_args()
        updated_option = OptionService.update_option(option_id, args['name'])
        if updated_option:
            return {'id': str(updated_option.id), 'name': updated_option.name}
        return {'message': 'Option not found'}, 404

    def delete(self, option_id):
        if OptionService.delete_option(option_id):
            return {'message': 'Option deleted successfully'}, 204
        return {'message': 'Option not found'}, 404
