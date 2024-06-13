import PyPDF2

gv_number_pages = 0
gv_list_all_pages = []

def reducir_pdf(ruta_pdf_original, ruta_pdf_reducido, paginas_a_imprimir, paginas_a_eliminar):
    with open(ruta_pdf_original, 'rb') as pdf_original:
        pdf_reader = PyPDF2.PdfReader(pdf_original)
        pdf_writer = PyPDF2.PdfWriter()
        #Get number of pages document
        gv_number_pages = len(pdf_reader.pages)
        gv_list_all_pages = generate_all_pages(gv_number_pages)

        if len(paginas_a_eliminar) > 0:
            #delete pages from gv_list_all_pages   
            paginas_a_imprimir = eliminar_numeros_de_lista(gv_list_all_pages, paginas_a_eliminar)
        for num_pagina in range(gv_number_pages):
            if num_pagina in paginas_a_imprimir:
                pagina = pdf_reader.pages[num_pagina]
                pdf_writer.add_page(pagina)

        with open(ruta_pdf_reducido, 'wb') as pdf_reducido:
            pdf_writer.write(pdf_reducido)
        print("generado archivo:", pdf_reducido)
#######################################################################################
def find_common_elements(list1, list2):
    """Finds common elements between two lists using sets.

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        A set containing the common elements, or an empty set if there are none.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2) 
########################################################################################
def generate_all_pages(top):
    """Genera una lista de números desde 0 hasta el límite especificado.

    Args:
        limite (int): El número máximo (inclusive) hasta el cual generar la lista.

    Returns:
        list: Una lista de números enteros desde 0 hasta el límite.
    """
    lista_numeros = []
    
    for numero in range(top):  #No incluir el limite
        lista_numeros.append(numero)
    return lista_numeros
############################################################################################
def eliminar_numeros_de_lista(lista_original, lista_a_eliminar):
  """Elimina los números de 'lista_original' que aparecen en 'lista_a_eliminar'.

  Args:
      lista_original: La lista de números original.
      lista_a_eliminar: La lista de números a eliminar.

  Returns:
      Una nueva lista con los números de 'lista_original' que no están en 'lista_a_eliminar'.
  """

  conjunto_a_eliminar = set(lista_a_eliminar)  # Convertir a conjunto para búsquedas rápidas
  lista_filtrada = []

  for num in lista_original:
    if num not in conjunto_a_eliminar:
      lista_filtrada.append(num)

  return lista_filtrada


########################################################################################
# Ejemplo de uso
ruta_pdf_original = 'c:\\Users\\jjair\\Downloads\\original.pdf'
ruta_pdf_reducido = 'c:\\Users\\jjair\\Downloads\\mi_pdf_reducido.pdf'
gv_paginas_a_eliminar = [0, 1, 7, 8]  # Páginas 1, 2, 8 y 9 (empezando desde 0)
gv_paginas_a_eliminar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11,  12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                      36, 37, 38, 39, 40, 41,  42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62 ]
#gv_paginas_a_eliminar = []
gv_paginas_a_imprimir = [0, 73, 84, 85]
gv_paginas_a_imprimir = []

#validate if the lists have common elements
comunes = find_common_elements(gv_paginas_a_eliminar, gv_paginas_a_imprimir) 
print('comunes', comunes)
if len(comunes) == 0:
    if len(gv_paginas_a_eliminar) > 0 and len(gv_paginas_a_imprimir) > 0:
        print('Listas a imprimir y a eliminar no pueden existir simultaneamente')
    else:
        reducir_pdf(ruta_pdf_original, ruta_pdf_reducido, gv_paginas_a_imprimir, gv_paginas_a_eliminar)
else:
    print('no se puede eliminar e imprimir la misma pagina al mismo tiempo!', comunes)
print('Fin del recorte')