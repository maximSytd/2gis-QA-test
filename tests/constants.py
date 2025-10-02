from http import HTTPStatus

from d42 import schema

OkStatusSchema = schema.int(HTTPStatus.OK)
UnauthorizedStatusSchema = schema.int(HTTPStatus.UNAUTHORIZED)
BadRequestStatusSchema = schema.int(HTTPStatus.BAD_REQUEST)
ForbiddenStatusSchema = schema.int(HTTPStatus.FORBIDDEN)
UnprocessableEntityStatusSchema = schema.int(HTTPStatus.UNPROCESSABLE_ENTITY)
InternalServerErrorStatusSchema = schema.int(HTTPStatus.INTERNAL_SERVER_ERROR)
NoContentStatusSchema = schema.int(HTTPStatus.NO_CONTENT)
NotFoundStatusSchema = schema.int(HTTPStatus.NOT_FOUND)
ExpectationFailedStatusSchema = schema.int(HTTPStatus.EXPECTATION_FAILED)

__all__ = [
    'OkStatusSchema',
    'UnauthorizedStatusSchema',
    'BadRequestStatusSchema',
    'ForbiddenStatusSchema',
    'UnprocessableEntityStatusSchema',
    'InternalServerErrorStatusSchema',
    'NoContentStatusSchema',
    'NotFoundStatusSchema',
]