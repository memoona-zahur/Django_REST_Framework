from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializer import TodoSerializer


@api_view(["GET", "POST", "PATCH"])
def home(request):
    if request.method == "GET":
        return Response(
            {
                "status": 200,
                "message": "Yes! Django REST Framework is working perfectly!!!",
                "method_called": "You called GET method",
            }
        )
    elif request.method == "POST":
        return Response(
            {
                "status": 200,
                "message": "Yes! Django REST Framework is working perfectly!!!",
                "method_called": "You called POST method",
            }
        )
    elif request.method == "PATCH":
        return Response(
            {
                "status": 200,
                "message": "Yes! Django REST Framework is working perfectly!!!",
                "method_called": "You called PATCH method",
            }
        )
    else:
        return Response(
            {
                "status": 400,
                "message": "Yes! Django REST Framework is working perfectly!!!",
                "method_called": "You called invalid method",
            }
        )


@api_view(["GET"])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)
    return Response(
        {"status": True, "message": "Todo list is fetched", "data": serializer.data}
    )


@api_view(["POST"])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Successfully data is received",
                    "data": serializer.data,
                }
            )

        return Response(
            {"status": False, "message": "Invalid data", "data": serializer.errors}
        )
    except Exception as e:
        print(e)
    return Response(
        {
            "status": False,
            "message": "Something went wrong",
        }
    )


@api_view(["PATCH"])
def patch_todo(request):
    try:
        data = request.data
        if not data.get("uid"):
            return Response({"status": False, "message": "uid is required", "data": {}})
        obj = Todo.objects.get(uid=data.get("uid"))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Successfully data is received",
                    "data": serializer.data,
                }
            )
        return Response(
            {"status": False, "message": "Invalid data", "data": serializer.errors}
        )
    except Exception as e:
        print(e)
    return Response({"status": False, "message": "Invalid uid", "data": {}})


class TodoView(APIView):
    def get(self, request):
        # return Response(
        #     {
        #         "status": 200,
        #         "message": "Yes! Django REST Framework is working perfectly!!!",
        #         "method_called": "You called GET method",
        #     }
        # )

        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)
        return Response(
            {"status": True, "message": "Todo list is fetched", "data": serializer.data}
        )

    def post(self, request):
        # return Response(
        #     {
        #         "status": 200,
        #         "message": "Yes! Django REST Framework is working perfectly!!!",
        #         "method_called": "You called POST method",
        #     }
        # )

        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Successfully data is received",
                        "data": serializer.data,
                    }
                )

            return Response(
                {"status": False, "message": "Invalid data", "data": serializer.errors}
            )
        except Exception as e:
            print(e)
        return Response(
            {
                "status": False,
                "message": "Something went wrong",
            }
        )


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
