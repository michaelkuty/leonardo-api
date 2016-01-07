
import graphene
from django.contrib.auth.models import User as DjangoUser
from graphene import relay, resolve_only_args
from graphene.contrib.django import DjangoConnection, DjangoNode


schema = graphene.Schema(name='Leonado CMS Relay Schema')


class Connection(DjangoConnection):
    total_count = graphene.Int()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())


class User(DjangoNode):
    '''An individual person or character within the Star Wars universe.'''
    class Meta:
        model = DjangoUser
    connection_type = Connection
    data = graphene.String()


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()


class AddUser(graphene.Mutation):
    '''
    .. code-block:: json

        query {
            addUser(username:"petr", email: "sadp@asd.cz") {
                    username, email
                }
        }

    '''

    class Input:
        data = graphene.Argument(UserInput)
        username = graphene.String()
        password = graphene.String()
        #data = graphene.String()
        date = graphene.String()
        _id = graphene.String()

    data = graphene.String()
#    date = graphene.String()
#    name = graphene.String()
    password = graphene.String()
    username = graphene.String()
    email = graphene.String()

    @classmethod
    def mutate(cls, query, args, info):
        args.pop('name', None)
        args.pop('date', None)
        #user = DjangoUser(**args)
        # user.save()
        return AddUser(**args)


class UserMutations(graphene.ObjectType):
    add_user = graphene.Field(AddUser)


class Query(graphene.ObjectType):

    users = graphene.List(User)
    # relay.ConnectionField(User)

    user = relay.NodeField(User)

    node = relay.NodeField()

    get_user = graphene.Field(User,
                              id=graphene.String().NonNull)

    def resolve_users(self, *args, **kwargs):
        return DjangoUser.objects.all()

    def resolve_get_user(self, args, info):
        return DjangoUser.objects.get(id=args.get('id'))

    def resolve_viewer(self, *args, **kwargs):
        return self


schema.query = Query
schema.mutation = UserMutations
