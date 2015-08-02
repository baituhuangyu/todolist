# -*-coding: utf-8 -*-

import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext, Template, Context, loader
from models import Todo
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import re

logger = logging.getLogger('blog.views')


def index(request):
    # todoid = request.POST['id']
    # todoname = request.POST['name']
    # todostatue = request.POST['statue']
    try:
        userinfo=request.META.get('HTTP_USER_AGENT')
        print(userinfo)
        rep=r'MSIE\s(8|7|6|5|4|3|2|1)\.\d'
        if re.search(rep, userinfo):
            print('IE too low!')
            IEBelow9=True
            return render_to_response('index.html',
                                      {'IEBelow9': IEBelow9},
                                      context_instance=RequestContext(request))
        else:
            # IE=False
            notlist = Todo.objects.filter(statue=0)
            finishlist = Todo.objects.filter(statue=1)
            notpaginator = Paginator(notlist, 3)
            finishpaginator = Paginator(finishlist, 3)
            try:
                anotpage = int(request.GET.get('notpage', 1))
                afinishpage = int(request.GET.get('finishpage', 1))
                nottodo = notpaginator.page(anotpage)
                finish = finishpaginator.page(afinishpage)
            # print(Todo.objects.order_by('id').reverse()[0].id + 1)
            except (EmptyPage, InvalidPage, PageNotAnInteger):
                nottodo = notpaginator.page(1)
                finish = finishpaginator.page(1)
            return render_to_response('index.html',
                                      {'nottodo': nottodo, 'finish': finish},
                                      context_instance=RequestContext(request))
    except Exception:
        print('unknow ')
        raise Http404

def deletelist(request, id=""):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/index/')
    notlist = Todo.objects.filter(statue=0)
    finish = Todo.objects.filter(statue=1)
    return render_to_response('index.html',
                              {'notlist': notlist, 'finish': finish},
                              context_instance=RequestContext(request))



def finish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.statue == '0':
        todo.statue = '1'
        todo.save()
        return HttpResponseRedirect('/index/')
    notlist = Todo.objects.filter(statue=0)
    finish = Todo.objects.filter(statue=1)
    return render_to_response('index.html',
                              {'notlist': notlist, 'finish': finish},
                              context_instance=RequestContext(request))

def nofinish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.statue == '1':
        todo.statue = '0'
        todo.save()
        return HttpResponseRedirect('/index/')
    notlist = Todo.objects.filter(statue=0)
    finish = Todo.objects.filter(statue=1)
    return render_to_response('index.html',
                              {'notlist': notlist, 'finish': finish},
                              context_instance=RequestContext(request))

def addtodo(request):
    if 'Item' in request.GET and request.GET['Item']:
        newname = request.GET['Item']
        newstatue = '0'
        # print('1')
        newid = Todo.objects.order_by('id').reverse()[0].id+1
        todo = Todo(id=newid, name=newname, statue=newstatue)
        todo.save()
        # NOtE:重定向至首页，安全一些
        return HttpResponseRedirect('/index/')
        ##or：发送请求至首页与重定向有区别
        # return index(request)

        # notlist = Todo.objects.filter(statue=0)
        # finishlist = Todo.objects.filter(statue=1)
        # notpaginator = Paginator(notlist, 3)
        # finishpaginator = Paginator(finishlist, 3)
        # try:
        #     anotpage = int(request.GET.get('notpage', 1))
        #     afinishpage = int(request.GET.get('finishpage', 1))
        #     nottodo = notpaginator.page(anotpage)
        #     finish = finishpaginator.page(afinishpage)
        # # print(Todo.objects.order_by('id').reverse()[0].id + 1)
        # except (EmptyPage, InvalidPage, PageNotAnInteger):
        #     nottodo = notpaginator.page(1)
        #     finish = finishpaginator.page(1)
        # return render_to_response('index.html',
        #                       {'nottodo': nottodo, 'finish': finish},
        #                       context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/index/')
        # return index(request)


def edittodo(request, id=''):
    #GET方法
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=id)
            # print('1')
        except Exception:
            # print('2')
            return HttpResponseRedirect('/index/')
        name = request.POST['Item']
        # statue = request.POST['statue']
        todo.name = name
        # todo.statue = statue
        # print('3')
        todo.save()
        return HttpResponseRedirect('/index/')
    else:
        try:
            todo = Todo.objects.get(id=id)
            # print('4')
        except Exception:
            # print('5')
            raise Http404
        return render_to_response('edit.html',
                                  {'todo': todo},
                                  context_instance=RequestContext(request))

#just for test not use
# 弹出式增加tolist
# def addtodo(request):
#     if request.method == 'POST':
#         newname = request.POST['name']
#         newstatue = '0'
#         newid = Todo.objects.get(id='1')
#         todo = Todo(id=newid, name=newname, statue=newstatue)
#         todo.save()
#         notlist = Todo.objects.filter(statue=0)
#         finish = Todo.objects.filter(statue=1)
#         return render_to_response('index.html',
#                               {'notlist': notlist, 'finish': finish},
#                               context_instance=RequestContext(request))
#     else:
#         notlist = Todo.objects.filter(statue=0)
#         finish = Todo.objects.filter(statue=1)
#         return render_to_response('index.html',
#                               {'notlist': notlist, 'finish': finish},
#                               context_instance=RequestContext(request))

# def writetobd(request):
#     content=request.POST.get('nottodo.name')
#
# def current_url_view_good(request):
#     print request.get_host()
#     print request.get_full_path()
#     print request.is_secure()
#     return HttpResponse("Welcome to the page at %s" % request.path)

# def ua_display_good2(request):
#     ua = request.META.get('HTTP_USER_AGENT', 'unknown')
#     return HttpResponse("Your browser is %s" % ua)

# def display_meta(request):
#     values = request.META.items()
#     values.sort()
#     html = []
#     for k, v in values:
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#     print '<table>%s</table>' % '\n'.join(html)
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))
#
# def search_form(request):
#     return render_to_response('search_form.html')
#
# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)
#
#
# def nottodolist(request):
#     nottodolist = Todo.objects.filter(statue=0)
#     return render_to_response('nottodo.html',
#                               {'nottodolist': nottodolist},
#                               context_instance=RequestContext(request))
#
# def finishlist(request):
#     finish = Todo.objects.filter(statue=1)
#     return render_to_response('finishtodo.html',
#                               {'finish': finish},
#                               context_instance=RequestContext(request))
#
#
# def index4(request):
#     todolist = Todo.objects.filter(statue=0)
#     paginator = Paginator(todolist, 3)
#     try:
#         apage = int(request.GET.get('page', 1))
#         todolist = paginator.page(apage)
#     # print(Todo.objects.order_by('id').reverse()[0].id + 1)
#     except (EmptyPage, InvalidPage, PageNotAnInteger):
#         todolist = paginator.page(1)
#
#     return render_to_response('index4.html',
#                               {'todolist': todolist},
#                               context_instance=RequestContext(request))


# def nottodochangetofinshtodo(request, id=''):
#     nottodo = Todo.objects.get(id=id)
#     if nottodo.statue == '1':
#         nottodo.statue = '0'
#         nottodo.save()
#         return HttpResponseRedirect('/nottodos/')
#     nottodolist = Todo.objects.filter(statue=0)
#     return render_to_response('index.html', {'nottodolist': nottodolist},
#                               context_instance=RequestContext(request))
#
#
# def updatetodo(request, id=''):
#     if request.method == 'POST':
#         try:
#             todo = Todo.objects.get(id=id)
#         except Exception:
#             return HttpResponseRedirect('/nottodos/')
#         anottodo = request.POST['nottodo']
#         todo.list = anottodo
#         todo.save()
#         return HttpResponseRedirect('/nottodos/')
#     else:
#         try:
#             nottodo = Todo.objects.get(id=id)
#         except Exception:
#             raise Http404
#         return render_to_response('index.html', {'nottodo': nottodo},
#             context_instance=RequestContext(request))