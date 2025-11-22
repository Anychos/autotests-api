from pydantic import BaseModel, Field, ConfigDict


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

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int = Field(default=None, alias='maxScore')
    min_score: int = Field(default=None, alias='minScore')
    order_index: int = Field(default=None, alias='orderIndex')
    description: str | None
    estimated_time: str = Field(default=None, alias='estimatedTime')

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