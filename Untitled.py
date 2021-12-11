#!/usr/bin/env python
# coding: utf-8

# In[155]:


V1=0.000 
V2=0.0000
CP=0
RF="S"
QC=0
VDP=50
VTV=0


# In[157]:


print ("Olá seja bem vindo, por favor comece a passar os produtos")
V1=float(input())
while (V2!="0"):
    print ("Proximo produto, ou 0 para finalizar")
    V2=(input())
    V1=float(V1)+ float(V2)
    CP=CP+1
    
if (V1<VDP):
    print ("Foi dado o desconto de 5% pelo valor da compra ")
    V1= V1-(V1*0.05)

if(V1 == VDP):
        print ("Foi dado o desconto de 10% pelo valor da compra ")
        V1= V1-(V1*0.1)

if(V1>VDP):
    print ("Foi dado o desconto de 20% pelo valor da compra ")
    V1= V1-(V1*0.2)
    
print("O valor final ficou em",V1)
print("Você acumulou",CP," ponto's com essa compra.Acumule-os para ganhar premios!!")


  
print ("Funcioario do mercado,o pagamento foi efetivado? 1 para sim e 2 para não")
RF=(input())
if (RF=="1"):
    print("Obrigado e volte sempre!")
    VTV=V1+VTV
    QC= QC+1
    print("Tivemos",QC," satisfeitos hoje")
else:
    print("Nosso mercado conta com o serviço de reserva por 3 horas para o cliente, se preferir fale com o funcionario e ele o ajudará")
V2=0
CP=0
print("Conseguimos até agora",VTV," em vendas")




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




