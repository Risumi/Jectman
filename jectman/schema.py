import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Project, Backlog, Sprint,User,Epic
from graphql_relay.node.node import from_global_id
from django.db.models import Q

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class BacklogType(DjangoObjectType):
    class Meta:
        model = Backlog

class SprintType(DjangoObjectType):
    class Meta:
        model = Sprint

class UserType(DjangoObjectType):
    class Meta:
        model = User

class EpicType(DjangoObjectType):
    class Meta:
        model = Epic


class CreateProject(graphene.Mutation):
    id = graphene.String()
    name = graphene.String()    
    description = graphene.String()
    status = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        description = graphene.String()
        status = graphene.String()    

    #3
    def mutate(self, info, id, name,description,status):
        project = Project(id=id, name=name,description=description,status=status)
        project.save()

        return CreateProject(
            id=project.id,
            name=project.name,
            description=project.description,
            status=project.status            
        )
class CreateSprint(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    begindate = graphene.Date()
    enddate = graphene.Date()
    goal = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        begindate = graphene.Date()
        enddate = graphene.Date()
        goal = graphene.String() 

    #3
    def mutate(self, info, id, id_project,begindate,enddate,goal):
        project = Project(id=id_project)
        sprint = Sprint(id=id, id_project=project,begindate=begindate,enddate=enddate,goal=goal)
        sprint.save()

        return CreateSprint(
            id = sprint.id,
            id_project = project.id,
            begindate = sprint.begindate,
            enddate = sprint.enddate,
            goal = sprint.goal             
        )

class CreateBacklogSprint(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()
    id_sprint = graphene.String()
    id_epic = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    description = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()
        id_sprint = graphene.String() 
        id_epic = graphene.String()
        name = graphene.String()        
        status = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        description = graphene.String()

    #3
    def mutate(self, info, id,id_project,id_sprint,id_epic,name,status,begindate,enddate,description):
        project = Project(id=id_project)
        sprint = Sprint(id=id_sprint)
        epic = Epic(id=id_epic)
        backlog = Backlog(id=id,id_project=project,id_sprint=sprint,id_epic=epic,name=name,status=status,begindate=begindate,enddate=enddate,description=description)        
        backlog.save()
        return CreateBacklog(
            id = backlog.id,
            id_project = project.id,
            id_sprint = sprint.id,
            id_epic = epic.id,
            name = backlog.name,
            status = backlog.status,
            begindate = backlog.begindate,
            enddate = backlog.enddate,
            description = backlog.description
        )

class CreateBacklogSprintNull(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()
    # id_sprint = graphene.String()
    id_epic = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    description = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()
        # id_sprint = graphene.String() 
        id_epic = graphene.String()
        name = graphene.String()        
        status = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        description = graphene.String()

    #3
    def mutate(self, info, id,id_project,id_epic,name,status,begindate,enddate,description):
        project = Project(id=id_project)
        sprint = None
        epic = Epic(id=id_epic)
        backlog = Backlog(id=id,id_project=project,id_sprint=sprint,id_epic=epic,name=name,status=status,begindate=begindate,enddate=enddate,description=description)        
        backlog.save()
        return CreateBacklogSprintNull(
            id = backlog.id,
            id_project = project.id,
            # id_sprint = sprint,
            id_epic = epic.id,
            name = backlog.name,
            status = backlog.status,
            begindate = backlog.begindate,
            enddate = backlog.enddate,
            description = backlog.description
        )

class CreateBacklog(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    id_epic = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    description = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()        
        id_epic = graphene.String()
        name = graphene.String()        
        status = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        description = graphene.String()

    #3
    def mutate(self, info, id,id_project,id_epic,name,status,begindate,enddate,description):
        project = Project(id=id_project)        
        epic = Epic(id=id_epic)
        backlog = Backlog(id=id,id_project=project,id_epic=epic,name=name,status=status,begindate=begindate,enddate=enddate,description=description)        
        backlog.save()
        return CreateBacklog(
            id = backlog.id,
            id_project = project.id,  
            id_epic = epic.id,
            name = backlog.name,
            status = backlog.status,
            begindate = backlog.begindate,
            enddate = backlog.enddate,
            description = backlog.description
        )

class CreateUser(graphene.Mutation):
    email = graphene.String()
    nama = graphene.String()    
    password = graphene.String()            
    #2
    class Arguments:
        email = graphene.String()
        nama = graphene.String()    
        password = graphene.String()                

    #3
    def mutate(self, info, email,nama,password):        
        user = User(email=email,nama=nama,password=password)        
        user.save()
        return CreateUser(
            email = user.email,
            nama = user.nama,            
            password = user.password
        )

class CreateEpic(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    name = graphene.String()            
    description = graphene.String()            
    status = graphene.String()            
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        name = graphene.String()            
        description = graphene.String()            
        status = graphene.String()   
    #3
    def mutate(self, info, id,id_project,name,description,status):        
        project = Project(id=id_project)
        epic = Epic(id=id,id_project=project,name=name,description=description,status=status)        
        epic.save()
        return CreateEpic(
            id = epic.id,
            id_project = project.id,
            name = epic.name,
            description = epic.description,
            status = epic.status
        )

class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_backlog = CreateBacklog.Field()
    create_backlogsprint = CreateBacklogSprint.Field()
    create_backlogsprintnull = CreateBacklogSprintNull.Field()
    create_sprint = CreateSprint.Field()
    create_user = CreateUser.Field()
    create_epic = CreateEpic.Field()

class Query(object):
    project= graphene.List(ProjectType)    
    backlog = graphene.List(BacklogType, id=graphene.String())
    backlogE=graphene.List(BacklogType,id_epic=graphene.String())
    sprint = graphene.List(SprintType, id=graphene.String())    
    epic = graphene.List(EpicType, id=graphene.String())
    user = graphene.List(UserType, email=graphene.String(), password=graphene.String())    
    
    def resolve_project(self, info, **kwargs):
        return Project.objects.all()

    def resolve_backlog(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id )                   
                )
                return Backlog.objects.filter(filter)
            return Backlog.objects.all()    
    

    def resolve_backlogE(self, info, id_epic=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q( id_epic__id__iexact = id_epic)                   
                )
                return Backlog.objects.filter(filter)
            return Backlog.objects.all()    

    def resolve_sprint(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Sprint.objects.filter(filter)
            return Sprint.objects.all()       

    def resolve_epic(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Epic.objects.filter(filter)
            return Epic.objects.all()  
            
    def resolve_user(self, info, email=None, password=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(email__exact=email,password__exact=password)                    
                )
                return User.objects.filter(filter)
            return User.objects.all()  