"""
1. Newspaper.objects.get(pk=1).journalist
"""

"""
2. Newspaper.objects.filter(journalist__contains='Laney Mccullough').count()
"""

"""
3. Newspaper.objects.order_by('-pk').values()
"""


"""
4. Newspaper.objects.order_by('-created_at').values()
"""

"""
5. Newspaper.objects.filter(journalist__contains='Britney').count()
"""

"""
6. Newspaper.objects.filter(journalist__in=['Britney Mahoney','Arianna Walls','Carl Short']).count()
"""

"""
7. import datetime
    start_date = datetime.datetime(2000,1,1,0,0,0)
    end_date = datetime.datetime(2023,3,28,0,0,0)
    Newspaper.objects.filter(created_at__range=(start_date, end_date)).count()
"""

"""
8. Newspaper.objects.order_by('-pk')[:1].values('title','content','journalist')
"""