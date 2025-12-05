from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.base_assertions import assert_value


def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует запросу.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_value(response.course.title, request.title, "title")
    assert_value(response.course.max_score, request.max_score, "max_score")
    assert_value(response.course.min_score, request.min_score, "min_score")
    assert_value(response.course.description, request.description, "description")
    assert_value(response.course.estimated_time, request.estimated_time, "estimated_time")