from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
import random
# Create your views here.
def home(request):
    context={'categories' : Category.objects.all()}
    selected_category = request.GET.get('category')
    if selected_category:
        #print(selected_category)
        return redirect(f"/quiz/?category={selected_category}")

    return render(request,'home.html', context)

def quiz(request):
    selected_category = request.GET.get('category')
    #print(selected_category)
    if selected_category :
        # Filter questions based on the selected category
        questions = Question.objects.filter(category__category_name__icontains=selected_category)
        #print(questions)
        questions=list(questions)
        question_with_answer={}
        #print(questions)
        for question in questions:
            #answers=Answer.objects.filter(question=question)
            
            #is_corr=Question.get_answer(question)
            #print(answers)
            answers=Question.get_answer(question)
            new_ans={}
            for ans in answers:
                k=0
                v=''
                for key, value in ans.items():
                    if key=='answer':
                        k=value
                    else:
                        v=value
                        new_ans[k]=v
                    #print(f'{key}: {value}')
                #print(new_ans)
                #print(ans)
            #print(answers)
            #print(question)
            #print(is_corr)
            
            question_with_answer[question]=new_ans
        print(question_with_answer)
        context={'question_with_answers' : question_with_answer}

        return render(request,'quiz.html', context)
    else:
        raise Http404("Category not specified.")

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs=list(question_objs)
        data=[]
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                'category': question_obj.category.category_name,
                'question': question_obj.question,
                'marks': question_obj.marks,
                'answer': question_obj.get_answer()
            })

        payload={'Status':True,'data': data}    
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse('An error Occured')