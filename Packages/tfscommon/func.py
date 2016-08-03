# -*-coding:utf8-*-
import subprocess,sys,datetime,re
def _execute_command(args=[],working_dir=""):
        process = subprocess.Popen(args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=working_dir)
        output, error = process.communicate()
        return (output.decode("gbk"), error)
def log(msg):
    sys.stdout.write("%s\n" % msg)

def makecontent(stdout):
    a = u'签入说明'+r':[\s\S]*?'+u'性能审阅者'+r'[\s\S]*?(?=[\r\n\t])'
    b=r'------[\s\S]*?('+u'项'+r':)'
    c=r'(\r\n){1,}'
    d=r'(?<=\r\n)[\s\S]*?(?=\$)'
    e=r'^[^$][\s\S]*?[\r\n]'
    handleRst=re.sub(a,"",stdout)
    handleRst=re.sub(b,"",handleRst)
    handleRst=re.sub(c,r'\r\n',handleRst)
    handleRst=re.sub(d,r'',handleRst)
    print(handleRst)
    # handleRst=re.sub(e,r'ssssssssssssssss',handleRst)

    # 预处理数据
    outputStr=handleRst
    ilist=handleRst.split("\r\n")
    # ilist=[]
    # for r in output2.find_all('^'):
    #     w=output2.line(r)
    #     g=output2.substr(w)
    #     if(g.strip()!=""):
    #         ilist.append(g)
    ilist=[i for i in ilist if i.strip()!=""]
    ilist.sort()
    ilist=list(set(ilist))
    ilist=sorted(ilist,key=lambda i : i)
    # return ("\n".join(ilist),outputStr)
    return (outputStr,0)


def recentTimestr(int):
	return (datetime.timedelta(minutes=-int)+datetime.datetime(2014,12,12).now()).strftime("D%Y-%m-%dT%H:%M:%S")+"~"+datetime.datetime(2014,12,12).now().strftime("D%Y-%m-%dT%H:%M:%S")
