import iris
from datetime import date

from grongier.pex import BusinessOperation
from grongier.pex import Utils


from msg import (CreateUserRequest, CreateUserResponse, GetUserRequest, GetUserResponse)

from obj import User

# > The CrudUser class is a business operation that handles Create, Update, Get and GetAll requests
# for a User object
class CrudUser(BusinessOperation):

    def on_message(self, request):
        return 

    def create_user(self,request:CreateUserRequest):
        """
        > Create a new user in the database and return the new user's ID
        
        :param request: The request object that was passed in from the client
        :type request: CreateUserRequest
        :return: The ID of the newly created user.
        """

        # sqlInsert = 'insert into Sample.User values (?,?,?,?,?)'
        # iris.sql.exec(sqlInsert,request.user.company,dob,request.user.name,request.user.phone,request.user.title)
        
        # IRIS ORM
        user = iris.cls('Sample.User')._New()
        if (v:=request.user.company) is not None: user.Company = v 
        if (v:=request.user.name) is not None: user.Name = v 
        if (v:=request.user.phone) is not None: user.Phone = v 
        if (v:=request.user.title) is not None: user.Title = v 
        if (v:=request.user.dob) is not None: user.DOB = iris.system.SQL.DATE(v.isoformat())

        Utils.raise_on_error(user._Save())
        
        return CreateUserResponse(
            user=User(
                id=int(user._Id()),
                dob=date.fromisoformat(iris.system.SQL.TOCHAR(user.DOB,"YYYY-MM-DD")),
                company=user.Company,
                name=user.Name,
                phone=user.Phone,
                title=user.Title
            )
        )

    def get_user(self,request:GetUserRequest):
        """
        > The function takes a `GetUserRequest` object, executes a SQL query, and returns a
        `GetUserResponse` object
        
        :param request: The request object that is passed in
        :type request: GetUserRequest
        :return: A GetUserResponse object
        """
        sql_select = """
            SELECT 
                Company, DOB, Name, Phone, Title, ID
            FROM Sample."User"
            where ID = ?
            """
        rs = iris.sql.exec(sql_select,request.id)
        response = GetUserResponse()
        for user in rs:
            try:
                dob = date.fromisoformat(iris.system.SQL.TOCHAR(user[1],"YYYY-MM-DD"))
            except:
                dob = ''
            response.user= User(id=user[5],company=user[0],dob=dob,name=user[2],phone=user[3],title=user[4])
        return response
