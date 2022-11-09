# Fjob_health = 0
#         Fjob_other = 0
#         Fjob_services = 0
#         Fjob_teacher = 0
#         match Fjob:
#             case "health": 
#                 Fjob_health = 1
#             case "other":
#                 Fjob_other = 1
#             case "services":
#                 Fjob_services = 1
#             case "teacher":
#                 Fjob_teacher = 1
#             case _:
#                 pass
        
#         Mjob_health = 0
#         Mjob_other = 0
#         Mjob_services = 0
#         Mjob_teacher = 0
#         match Mjob:
#             case "health": 
#                 Mjob_health = 1
#             case "other":
#                 Mjob_other = 1
#             case "services":
#                 Mjob_services = 1
#             case "teacher":
#                 Mjob_teacher = 1
#             case _:
#                 pass
        
#         higher_yes = 0
#         if higher == "yes":
#             higher_yes = 1

#         paid_yes = 0
#         if paid == "yes":
#             paid_yes = 1

#         school_MS = request.args.get('school_MS')
#         if school == "MS":
#             school_MS = 1
        
#         studytime = request.args.get('studytime')
#         failures = request.args.get('failures')
#         data = [[Fjob_health], [Fjob_other], 
#                 [Fjob_services], [Fjob_teacher],
#                 [Mjob_health], [Mjob_other],
#                 [Mjob_services], [Mjob_teacher],
#                 [failures], [higher_yes],
#                 [paid_yes], [school_MS], [studytime]]

# query_df = pd.DataFrame({
#             'Fjob' : pd.Series(Fjob), 
#             'Fjob_other' : pd.Series(Fjob_other), 
#             'Fjob_services': pd.Series(Fjob_services),
#             'Fjob_teacher': pd.Series(Fjob_teacher),
#             'Mjob_health': pd.Series(Mjob_health),
#             'Mjob_other': pd.Series(Mjob_other),
#             'Mjob_services': pd.Series(Mjob_services),
#             'Mjob_teacher': pd.Series(Mjob_teacher),
#             'failures': pd.Series(failures),
#             'higher_yes': pd.Series(higher_yes),
#             'paid_yes': pd.Series(paid_yes),
#             'school_MS': pd.Series(school_MS),
#             'studytime': pd.Series(studytime)
# })