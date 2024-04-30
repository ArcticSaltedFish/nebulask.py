# import os
# from flask import Flask, jsonify
# #from example.models import VirtualCharacter, Love
# from nebula_carina.models.model_builder import ModelBuilder
# from nebula_carina.models.models import EdgeModel
# from nebula_carina.ngql.query.conditions import Q

# #
# app = Flask(__name__)


# @app.get("/character/{character_id}")
# async def get_character(character_id: str):
#     return VirtualCharacter.objects.get(character_id)


# @app.get("/character/{character_id}/admirers")
# async def get_admirers(character_id: str):
#     return VirtualCharacter.objects.find_sources(character_id, Love, distinct=True)


# @app.get("/character/{character_id}/your-complex-relation")
# async def what_a_complex_human_relation(character_id: str):
#     return ModelBuilder.match(
#         '(v)-[e:love]->(v2)-[e2:love]->(v3)', {
#             'v': VirtualCharacter, 'e': EdgeModel, 'v2': VirtualCharacter,
#             'e2': EdgeModel, 'v3': VirtualCharacter
#         },
#         condition=Q(v__id=character_id),
#     )