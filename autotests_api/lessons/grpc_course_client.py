import grpc
from lessons import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)
# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print("Получен ответ от сервера:")
print(f"ID курса: {response.course_id}")
print(f"Название: {response.title}")
print(f"Описание: {response.description}")