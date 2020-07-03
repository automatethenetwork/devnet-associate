from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(
    access_token='MGRkZWFlODMtYTM4Ny00NTFlLTk2OTUtNWQzMjk1ZDM0NWVkOWU2ZjllMjItZDJj_PF84_consumer')

#### GET TEAM INFO ###

teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name') != 'CBT Team':
        create_team = api.teams.create('CBT Team')
        teamId = getattr(create_team, 'id')
    else:
        teamId = team.id

###### PEOPLE #####
print(api.people.me())
print(api.people.list())
#api.people.create(emails=['ben.finkel@cbtnuggets.com'], displayName='Ben Finkel', firstName='Ben',
#                  lastName='Finkel', roles=['Y2lzY29zcGFyazovL3VzL1JPTEUvaWRfZnVsbF9hZG1pbg'])

#### ROLES #####
roles = api.roles.list()
# print(roles)
#for role in roles:
#   print(role)

#### ROOMS #####
rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == 'CBT Room':
        evaluator = True
        roomId = room.id

if evaluator == False:
    new_room = api.rooms.create('CBT Room', teamId=teamId)
    roomId = new_room.id

#### MESSAGES ####
api.messages.create(roomId, text='Posted from the SDK Yaaaaaaaaaa')

# CLEANUP
# for room in rooms:
#     if getattr(room, 'title') == 'CBT Room':
#         api.rooms.delete(getattr(room, 'id'))

# for team in teams:
#     if getattr(team, 'name') == 'CBT Team':
#         api.teams.delete(getattr(team, 'id'))