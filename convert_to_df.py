## Code to Extract Data from Raw File Scrape

# profiles = []
# organizations = []
# experiences = []

# added_orgs = set()

# removeEmpty = lambda a : [x for x in a if x != '']

# for fname in tqdm(glob.glob('jumpstart/*.txt')):
#     with open(fname) as file:
#         data = json.load(file)
#         for row in data.get('results'):
#             profile_id = row.get('id')
#             profile = row.get('profile')

#             profiles.append({
#                 'id': profile_id,
#                 'first_name': row.get('first_name'),
#                 'last_name': row.get('last_name'),
#                 'profile_picture': row.get('profile_picture'),
#                 'linkedin_url': row.get('linkedin_url'),
#                 'college': profile.get('college'),
#                 'school': profile.get('school'),
#                 'majors': profile.get('majors'),
#                 'grad_year': profile.get('grad_year'),
#                 'degree_type': profile.get('degree_type'),
#                 'github_url': profile.get('github_url'),
#                 'about': profile.get('about'),
#                 'stackoverflow_url': profile.get('stackoverflow_url'),
#                 'personal_website_urls': removeEmpty(profile.get('personal_website_urls')),
#                 'passion_project_urls': removeEmpty(profile.get('passion_project_urls')),
#                 'experience_count': len(profile.get('experience'))
#             })
            
#             for e in profile.get('experience'):
#                 org = e.get('organization')
#                 if org.get('id') not in added_orgs:
#                     added_orgs.add(org.get('id'))
#                     organizations.append({k: v for k, v in org.items()})
                    
#                 try: 
#                     location = e.get('location')
#                     city = location.get('city').get('value')
#                     coordinates = location.get('coordinates')
#                 except: 
#                     city = None
#                     coordinates = None
                    
#                 experiences.append({
#                     'id': e.get('id'),
#                     'profile': profile_id,
#                     'organization': e.get('organization').get('id'),
#                     'title': e.get('title'),
#                     'description': e.get('description'),
#                     'startDate': e.get('startDate'),
#                     'endDate': e.get('endDate'),
#                     'coordinates': coordinates,
#                     'city': city
#                 })


# profile_df = pd.read_json(json.dumps(profiles)).drop(['first_name', 'last_name', 'linkedin_url', 'passion_project_urls', 'personal_website_urls', 'profile_picture', 'stackoverflow_url'], axis=1)
# experiences_df = pd.read_json(json.dumps(experiences))
# orgs_df = pd.read_json(json.dumps(organizations))

# profile_df.to_csv('profiles_df.csv')
# experiences_df.to_csv('experiences_df.csv')
# orgs_df.to_csv('orgs_df.csv')
