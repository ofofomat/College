import graphene


class Query(graphene.ObjectType):
    who = graphene.String(name=graphene.String(default_value="Leia"))

    def resolve_who(root, info, name):
        return f'Hi {name}!'


schema = graphene.Schema(query=Query)
