import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound
from .models import Pokemon, User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_pokemons(request, user_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound("User not found")

    pokemons = Pokemon.objects.filter(user=user)
    pokemons_data = [
        {
            'id': pokemon.id,
            'nombre': pokemon.nombre,
            'tipo': pokemon.tipo,
            'nivel': pokemon.nivel
        }
        for pokemon in pokemons
    ]

    return JsonResponse({'pokemons': pokemons_data})

@csrf_exempt
def get_allpokemons(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    pokemons = Pokemon.objects.all()
    pokemons_data = [
        {
            'id': pokemon.id,
            'nombre': pokemon.nombre,
            'tipo': pokemon.tipo,
            'nivel': pokemon.nivel,
            'user_id': pokemon.user.id if pokemon.user else None
        }
        for pokemon in pokemons
    ]

    return JsonResponse({'pokemons': pokemons_data})

@csrf_exempt
def create_pokemon(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        data = json.loads(request.body)
        nombre = data['nombre']
        tipo = data['tipo']
        nivel = data['nivel']
        user_id = data.get('user_id')

        user = None
        if user_id:
            user = User.objects.get(id=user_id)

        pokemon = Pokemon.objects.create(
            nombre=nombre,
            tipo=tipo,
            nivel=nivel,
            user=user
        )

        return JsonResponse({
            'id': pokemon.id,
            'nombre': pokemon.nombre,
            'tipo': pokemon.tipo,
            'nivel': pokemon.nivel,
            'user_id': pokemon.user.id if pokemon.user else None
        }, status=201)

    except (KeyError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid data")
    except User.DoesNotExist:
        return HttpResponseBadRequest("User not found")

@csrf_exempt
def update_pokemon(request, pokemon_id):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("Pokemon not found")

    try:
        data = json.loads(request.body)
        pokemon.nombre = data.get('nombre', pokemon.nombre)
        pokemon.tipo = data.get('tipo', pokemon.tipo)
        pokemon.nivel = data.get('nivel', pokemon.nivel)
        pokemon.save()

        return JsonResponse({
            'id': pokemon.id,
            'nombre': pokemon.nombre,
            'tipo': pokemon.tipo,
            'nivel': pokemon.nivel
        })

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid data")

@csrf_exempt
def delete_pokemon(request, pokemon_id):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed(['DELETE'])

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        pokemon.delete()
        return JsonResponse({'message': 'Pokemon deleted successfully'})

    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("Pokemon not found")
