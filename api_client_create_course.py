from clients.courses.courses_client import get_private_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_builder import AuthUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from clients.users.public_user_client import get_public_user_client


public_user_client = get_public_user_client()
create_user_request_body = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request_body)
print(create_user_response)

auth_user_dict = AuthUserSchema(
    email=create_user_request_body.email,
    password=create_user_request_body.password
)

files_client  = get_private_files_client(auth_user_dict)
courses_client = get_private_courses_client(auth_user_dict)

create_file_request = CreateFileRequestSchema(
    upload_file='./test_data/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print(create_file_response)

create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(create_course_response)