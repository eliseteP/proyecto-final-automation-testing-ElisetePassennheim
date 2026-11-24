import requests


URL = 'https://jsonplaceholder.typicode.com./post'


#res =requests.get(URL)

#print(res.json())
#POST
#datos = {
#    "title":"Mi primer envio de datos",
#    "body":"Estoy probando la Api de JsonLaceHolder",
#    "userId":1  
    
#}

#res= requests.post(URL,json=datos)
#print(res.json())
resp= requests.post(
    'https://dummyjson.com/auth/login',
    headers= {'Content-Type':'application/json'},
    json={
        'username':'emilys',
        'password':'emilyspass',
        'expiresInmins':30,
    },
    timeout=15,
)
print(resp.json())
print(resp.status_code)
    

#URL='https://regres.in/api/users'

#api_key = 'pub:acbe1a1d613f6d1c52150ad8dd514d06fceaa2b0f570bdcf858d1707aa45daae'
#headers={"x-api-key":api_key
#        }



#respuesta_get= requests.get(URL,headers=headers)

#print(respuesta_get.json())


URL='https://dummyjson.com/products'

print(" LISTA ORIGINAL DE PRODUCTOS")

respuesta_get=requests.get(URL, timeout=10)
print("Codigo HTTP:", respuesta_get.status_code)

productos=respuesta_get.json ()
indice_max=productos["products"]
print("Cantidad de productos:", len(indice_max))



nuevo_producto = {
    "title":"Brayann Farfan",
    "price":100,
    "category":"laptops"
}

respuesta_post = requests.post(f"{(URL)}/add",json=nuevo_producto)
print ("Codigo HTTP:", respuesta_post.status_code)

producto_creado=respuesta_post.json()



resp_get_final=requests.get(URL)
print ("Codigo HTTP:", resp_get_final.status_code)

datos_finales=resp_get_final.json()
productos_finales=datos_finales["products"]
productos_finales.append(producto_creado)
