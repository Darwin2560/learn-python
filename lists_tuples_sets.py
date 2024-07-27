# List

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Arl', 'Education']
# courses.append('Art')
# courses.insert(0, courses_2)
courses.extend(courses_2)
print(courses)
# courses.remove('Math')
popped = courses.pop()
print(popped)
courses.reverse()
print(courses)
courses.sort() # order
sorted_courses = sorted(courses) # return new list
print(courses[0:])
print(f'Nueva lista: {sorted_courses}')
print(courses.index('CompSci'))
print('Math' in courses)
for index, course in enumerate(courses, start=1):
    print(index, course)
courses_str = ', '.join(courses) # Convert to string separated by commas
print(courses_str)
new_list = courses_str.split(', ')
print(new_list)

list_nums = [1, 5, 2, 4, 3]
list_nums.sort(reverse=True) # reverse order
print(min(list_nums))
print(max(list_nums))
print(sum(list_nums))
print(list_nums)

# Tuples -> Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Set -> No repetition

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
