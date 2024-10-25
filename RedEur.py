import scrapy
import json
#europa siempre ha de ser el ultimo


class primerSpyder(scrapy.Spider):
    name='refeur'
    allowed_domains = ['redalyc.org','ebi.ac.uk']
    
    custom_settings = {
        'FEED_FORMAT': 'xlsx',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }
    def start_requests(self):
        data=self.dotos
        urll=(f'https://www.redalyc.org/service/r2020/getArticles/{data}/1/1/1/default')
        yield scrapy.Request(urll,callback=self.parse_rr)

    def parseura(self, response):
        pr= response.url
        dato=self.dotos
        data=self.datos
        if pr:
          mark=response.xpath('nextCursorMark/text()').get()
          count=response.xpath('hitCount/text()').get()
          #pagi=(f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=russo%20en%20venezuela&cursorMark={mark}&resultType=lite&format=xml')
          pagi=(f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={dato}&cursorMark={mark}&resultType=lite&format=xml')
          if mark:
            id=response.xpath('resultList/result/id/text()').getall()
            doi=response.xpath('resultList/result/doi/text()').getall()
            title=response.xpath('resultList/result/title/text()').getall()
            autor=response.xpath('resultList/result/authorString/text()').getall()
            nombreRevista=response.xpath('resultList/result/journalTitle/text()').getall()
            anopublicacion=response.xpath('resultList/result/pubYear/text()').getall()
            tipo=response.xpath('resultList/result/pubType/text()').getall()
            sour=response.xpath('resultList/result/source/text()').getall()
            open=response.xpath('resultList/result/isOpenAccess/text()').getall()
            sitas=response.xpath('resultList/result/citedByCount/text()').getall()
            for i,d,t,a,nr,an,ti,so,op,si in zip(id,doi,title,autor,nombreRevista,anopublicacion,tipo,sour,open,sitas):
              item={
                'Fuente':('europepmc'),
                'Doi': d,            
                'Autor':a,
                'Titulo':t,
                'Palabras_Claves':(''),
                'Tipo_Publicacion':ti,
                'Idioma':(''),
                'Link':(f'https://europepmc.org/article/{so}/{i}'),
                'Revista': nr,
                'Veces_citados':si,
                'Ano_Publicacion': an,
                'Open_access':op,   
                }
              yield item
            if id:
              yield scrapy.Request(url=pagi,callback=self.parseura)
            #else:
             # urll=(f'https://www.redalyc.org/service/r2020/getArticles/{dato}/1/100/1/default')
              #yield scrapy.Request(urll,callback=self.parse_rr)
          else:
            if count == '1':
              id=response.xpath('resultList/result/id/text()').get()
              doi=response.xpath('resultList/result/doi/text()').get()
              title=response.xpath('resultList/result/title/text()').get()
              autor=response.xpath('resultList/result/authorString/text()').get()
              nombreRevista=response.xpath('resultList/result/journalTitle/text()').get()
              anopublicacion=response.xpath('resultList/result/pubYear/text()').get()
              tipo=response.xpath('resultList/result/pubType/text()').get()
              sour=response.xpath('resultList/result/source/text()').get()
              open=response.xpath('resultList/result/isOpenAccess/text()').get()
              sitas=response.xpath('resultList/result/citedByCount/text()').get()
              item={
                  'Fuente':('europepmc'),
                  'Doi': doi,            
                  'Autor':autor,
                  'Titulo':title,
                  'Palabras_Claves':(''),
                  'Tipo_Publicacion':tipo,
                  'Idioma':(''),
                  'Link':(f'https://europepmc.org/article/{sour}/{id}'),
                  'Revista': nombreRevista,
                  'Veces_citados':sitas,
                  'Ano_Publicacion': anopublicacion,
                  'Open_access':open,   
                  }
              yield item
           #   urll=(f'https://www.redalyc.org/service/r2020/getArticles/{dato}/1/100/1/default')
            #  yield scrapy.Request(urll,callback=self.parse_rr)
            else:
              id=response.xpath('resultList/result/id/text()').getall()
              doi=response.xpath('resultList/result/doi/text()').getall()
              title=response.xpath('resultList/result/title/text()').getall()
              autor=response.xpath('resultList/result/authorString/text()').getall()
              nombreRevista=response.xpath('resultList/result/journalTitle/text()').getall()
              anopublicacion=response.xpath('resultList/result/pubYear/text()').getall()
              tipo=response.xpath('resultList/result/pubType/text()').getall()
              sour=response.xpath('resultList/result/source/text()').getall()
              open=response.xpath('resultList/result/isOpenAccess/text()').getall()
              sitas=response.xpath('resultList/result/citedByCount/text()').getall()
              for i,d,t,a,nr,an,ti,so,op,si in zip(id,doi,title,autor,nombreRevista,anopublicacion,tipo,sour,open,sitas):
                item={
                  'Fuente':('europepmc'),
                  'Doi': d,            
                  'Autor':a,
                  'Titulo':t,
                  'Palabras_Claves':(''),
                  'Tipo_Publicacion':ti,
                  'Idioma':(''),
                  'Link':(f'https://europepmc.org/article/{so}/{i}'),
                  'Revista': nr,
                  'Veces_citados':si,
                  'Ano_Publicacion': an,
                  'Open_access':op,   
                  }
                yield item

    def parse_rr(self,response):
      pr= response.url
      dato=self.dotos
      data=self.datos
      if pr:
        data=response.body
        dat=json.loads(data)
        rac=dat['totalResultados']
        print(rac)
        div =rac/1000
        oere=3/2
        dire=int(div)
        dar=type(div)
        daer=type(oere)
        print(dar)
        print(daer)
        print(oere)
        if dar == daer:
          print('si lo es')
          dirre=dire+1
        else:
          print('no lo es')
          dirre=dire
        print(dirre)
        for i in range(1,dirre+1):
        #for i in range(1,3):
          #url=(f'https://www.redalyc.org/service/r2020/getArticles/russo%20en%20venezuela/{i}/1000/1/default')
          urll=(f'https://www.redalyc.org/service/r2020/getArticles/{dato}/{i}/1000/1/default')
          yield scrapy.Request(url=urll,callback=self.parse_ar)
        url=(f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={dato}')
        yield scrapy.Request(url=url,callback=self.parseura)
      
    def parse_ar(self,response):
      pr= response.url
      #dato=self.dotos
      if pr:
        data=response.body
        dat=json.loads(data)
        #rac=dat['totalResultados']
        #url=(f'https://www.redalyc.org/service/r2020/getArticles/{dato}/1/{rac}/1/default')  
        for i in range(0,1000):
          anioArticulo= dat['resultados'][i]['anioArticulo']
          if anioArticulo:
            anioArticulo= dat['resultados'][i]['anioArticulo']
          else:
            anioArticulo= ""
          doiTitulo= dat['resultados'][i]['doiTitulo']
          if doiTitulo:
            doiTitulo= dat['resultados'][i]['doiTitulo']
          else:
            doiTitulo= ""
          autores= dat['resultados'][i]['autores']
          if autores:
            autores= dat['resultados'][i]['autores']
          else:
            autores= ""
          #contenido= dat['resultados'][i]['contenido']
          idiomaArticulo= dat['resultados'][i]['idiomaArticulo']
          if idiomaArticulo:
            idiomaArticulo= dat['resultados'][i]['idiomaArticulo']
          else:
            idiomaArticulo= ""
          nomRevista= dat['resultados'][i]['nomRevista']
          if nomRevista:
            nomRevista= dat['resultados'][i]['nomRevista']
          else:
            nomRevista= ""
          palabras= dat['resultados'][i]['palabras']
          if palabras:
            palabras= dat['resultados'][i]['palabras']
          else:
            palabras= ""
          titulo= dat['resultados'][i]['titulo']
          if titulo:
            titulo= dat['resultados'][i]['titulo']
          else:
            titulo= ""
          rutaArchiv= dat['resultados'][i]['rutaArchivo']
          if rutaArchiv:
            rutaArchiv= dat['resultados'][i]['rutaArchivo']
          else:
            rutaArchiv= ""
          ruta=rutaArchiv.replace("\\","/")      
          yield{
            'Fuente':('redalyc'),
            'Doi':doiTitulo,            
            'Autor':autores,
            'Titulo':titulo,
            'Palabras_Claves':palabras,
            'Tipo_Publicacion':(""),
            'Idioma':idiomaArticulo,
            'Link':(f'https://www.redalyc.org/pdf/{ruta}'),
            'Revista': nomRevista,
            'Veces_citados':(""),
            'Ano_Publicacion': anioArticulo,
            'Open_access':(""),
            }
