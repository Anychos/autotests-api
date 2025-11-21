from clients.courses.courses_client import get_private_courses_client, CreateCourseRequestBody
from clients.files.files_client import get_private_files_client, CreateFileRequestBody
from clients.private_builder import AuthUserDict
from clients.users.public_user_client import get_public_user_client, CreateUserRequestBody


email = 'test8@mail.ru'

public_user_client = get_public_user_client()
create_user_request_body = CreateUserRequestBody(
    email=email,
    password='password',
    lastName='lastName',
    firstName='firstName',
    middleName='middleName'
)
create_user_response = public_user_client.create_user(create_user_request_body)
print(create_user_response)

auth_user_Dict = AuthUserDict(
    email=email,
    password='password'
)

files_client  = get_private_files_client(auth_user_Dict)
courses_client = get_private_courses_client(auth_user_Dict)

create_file_request = CreateFileRequestBody(
    filename='image.png',
    directory='courses',
    upload_file='./test_data/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print(create_file_response)

create_course_request = CreateCourseRequestBody(
    title='title',
    maxScore=100,
    minScore=0,
    description='description',
    estimatedTime="one hour",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(create_course_response)