from pydantic import BaseModel, Field, ConfigDict
from tools.data_generator import fake


class GetExercisesRequestSchema(BaseModel):
    """
    Описание модели запроса на получение упражнений курса
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')

class GetExerciseRequestSchema(BaseModel):
    """
    Описание модели запроса на получение упражнения по его id
    """
    exercise_id: str

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание модели запроса на создание упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.description)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.description)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)

class ExerciseSchema(BaseModel):
    """
    Описание базовой модели упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class GetExercisesResponseSchema(BaseModel):
    """
    Описание модели ответа на получение упражнений
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание модели ответа на получение упражнения
    """
    exercises: ExerciseSchema

class CreateExercisesResponseSchema(BaseModel):
    """
    Описание модели ответа на создание упражнения
    """
    exercise: ExerciseSchema

class UpdateExercisesResponseSchema(BaseModel):
    """
    Описание модели ответа на обновление упражнения
    """
    exercise: list[ExerciseSchema]