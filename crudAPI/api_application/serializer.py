from .models import Todo


def todo_serializer(todos:list[Todo]) -> list[dict]:
    response = list()
    for todo in todos:
        todo_dict = {
            'id' : todo.id,
            'name': todo.name,
            'desc': todo.description,
            'created_at': str(todo.created_at),
            'completed': todo.completed
        }
        response.append(todo_dict)
    return response
