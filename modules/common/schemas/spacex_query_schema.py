from sgqlc.types import String, Type, Field, Int, ID, Boolean


class HeadquarterNode(Type):
    address = String
    city = String
    state = String


class CompanyNode(Type):
    name = String
    ceo = String
    coo = String
    cto = String
    cto_propulsion = Field(str, graphql_name="cto_propulsion")
    founder = String
    employees = Int
    founded = Int
    launch_sites = Field(str, graphql_name="launch_sites")
    test_sites = Field(str, graphql_name="test_sites")
    valuation = Int
    vehicles = Int
    headquarters = HeadquarterNode
    

class CompanyInvalidNode(Type):
    name = String
    ceo = String
    coo = String
    cto = String
    cto_propulsion = String
    founder = String
    employees = Int
    founded = Int
    launch_sites = String
    test_sites = String
    valuation = Int
    vehicles = Int
    headquarters = HeadquarterNode


class HistoryNode(Type):
    id = ID
    title = String
    details = String
    event_date_unix = Field(str, graphql_name="event_date_unix")
    event_date_utc = Field(str, graphql_name="event_date_utc")


class RocketNode(Type):
    id = ID
    name = String
    type = String
    active = Boolean
    company = String
    country = String
    description = String
    first_flight = Field(str, graphql_name="first_flight")
    cost_per_launch = Field(int, graphql_name="cost_per_launch")
    stages = Int
    boosters = Int
    success_rate_pct = Field(int, graphql_name="success_rate_pct")
    wikipedia = String


class RocketInvalidNode(Type):
    id = ID
    name = String
    type = String
    active = Boolean
    company = String
    country = String
    description = String
    first_flight = String
    cost_per_launch = Int
    stages = Int
    boosters = Int
    success_rate_pct = Int
    wikipedia = String


class Query(Type):
    company = Field(CompanyNode)
    history = Field(HistoryNode, args={'id': String})
    rocket = Field(RocketNode, args={'id': String})
    company_bad = Field(CompanyInvalidNode)
    rocket_bad = Field(RocketInvalidNode, args={'id': String})
