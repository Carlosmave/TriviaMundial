from django.shortcuts import render
from django.http import HttpResponse
from .models import questions, answers
# Create your views here.
def index(request):

    #Trivia=questions.objects.all()

    #Trivia=questions.objects.get(id=1)
    #context = {
    #    'trivia': Trivia
    #}
    return render(request, 'trivia/index.html')

#def details(request, id, tscore):
def details(request, id, ttlscore):

    if int(id)<31:
        triv = questions.objects.get(id=id)
        #answer = answers.objects.get(id=id)
        newid=int(id)+1
        #ttlscore=totalscore
        #strid=str(newid)
        #newscore=int(tscore)

        context={
        'triv':triv,
        'id': newid,
        'ttlscore':ttlscore
        #,
        #'tscore':newscore
        #,
        #'answ':answer
        }
        return render(request, 'trivia/details.html', context)
    else:
        context={
        'ttlscore':ttlscore
        #,
        #'tscore':newscore
        #,
        #'answ':answer
        }
        return render(request, 'trivia/scorescreen.html', context)

#def processing(request, option, id):
def processing(request, option, id, ttlscore):
    newid=int(id)+1
    triv = questions.objects.get(id=id)
    #answer = answers.objects.get(id=id)
    playeranswer=option
    objanswer = answers.objects.get(id=id)
    correctanswer = objanswer.answer.replace(" ", "")
    #correctanswer.replace(" ", "")
    questionscore = objanswer.score

    if correctanswer == playeranswer:
        context={
        'triv': triv,
        'message':'Respuesta Correcta',
        'qscore':questionscore,
        'ttlscore': int(ttlscore)+int(questionscore),
        'id':newid#,
        #'ttlscore':ttlscore
        }
        return render(request, 'trivia/outcome.html', context)
    else:
        context2={
        'triv': triv,
        'message':'Respuesta Incorrecta',
        'qscore':0,
        'ttlscore': ttlscore,
        'id':newid#,
        #'ttlscore':ttlscore
        }
        return render(request, 'trivia/outcome.html', context2)

    #context={
    #'triv': triv
    #}

    #return render(request, 'trivia/details.html', context)




#def details(request, id):
#    triv = questions.objects.get(id=id)
#    context={
#    'triv':triv
#    }
#    return render(request, 'trivia/details.html', context)
