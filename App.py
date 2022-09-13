from logging import PlaceHolder
from tkinter import Image
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Input, Output, State
from desplazamiento import desplazamiento
from sustitucion import VerifyKey, susDencript,susEncript
from permutacion import permutacion
import numpy as np
from vigenere import Vigenere
from afin import Afin
app = dash.Dash()

# Shift

@app.callback(Output("cipher_shift","children"),
                Input("c-shift-c","n_clicks"),
                State("t-shift-c","value"),
                State("k-shift-c","value"))
def shift_cipher(n,t,k):
    if not n:
        raise dash.exceptions.PreventUpdate

    data = t.replace(" ", "").lower()
    c = desplazamiento(data,int(k)).encriptar()
    return html.P(f"CIpher text is {c}")



@app.callback(Output("decrypt_shift","children"),
                Input("c-shift-d","n_clicks"),
                State("t-shift-d","value"),
                State("k-shift-d","value"))

def shift_decrypt(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    c = desplazamiento(t,int(k)).desencriptar()
    return html.P(f"Decrypted text is {c}")




# Substitution

@app.callback(Output("cipher_substitution","children"),
                Input("subs-c-b","n_clicks"),
                State("subs-c-t","value"),
                State("subs-c-k","value"))
def subs_cipher(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    t = susEncript(t,k)
    return html.P(f"Cipher text is {t}")


@app.callback(Output("decrypt_subs","children"),
                Input("subs-d-b","n_clicks"),
                State("subs-d-t","value"),
                State("subs-d-k","value"))

def subs_decrypt(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    t = susDencript(t,k)
    return html.P(f"Decrypted text is {t}")


#Permutation

@app.callback(Output("cipher_perm","children"),
                Input("perm-c-b","n_clicks"),
                State("perm-c-t","value"),
                State("perm-c-k","value"))
def perm_cipher(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    k = k.split(",")
    k = [int(a) for a in k]

    c = permutacion(t,k).encrypt()

    return html.P(f"Cipher text is {c}")


@app.callback(Output("decrypt_perm","children"),
                Input("perm-d-b","n_clicks"),
                State("perm-d-t","value"),
                State("perm-d-k","value"))
def perm_decrypt(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    k = k.split(",")
    k = [int(a) for a in k]

    l = permutacion(t,k).desencrypt()
    s = ""
    for i in l:
        s += l

    return html.P(f"Cipher text is {s}")


@app.callback(Output("cr_perm","children"),
                Input("perm-cr-b","n_clicks"),
                State("perm-cr-t","value"))
def perm_cr(n,t):
    if ((not n) or (not t)):
        raise dash.exceptions.PreventUpdate


    c = permutacion(t,[1]).cryptanalysis()

    return html.P(f"Possible plain texts are {' , '.join(c)}")

#Hill

@app.callback(Output("cipher_hill","children"),
                Input("hill-c-b","n_clicks"),
                State("up_img","filename"),
                State("hill-k","value"),
                State("hill-k-size","value"))


def hill_cipher(n,img,k,ks):
    if ((not n) or (not k) or (not img) or (not ks)):
        raise dash.exceptions.PreventUpdate

    #key = k.split(",")
    #key = [int(a) for a in key]
    #key = np.array(key).reshape((int(ks),int(ks)))
    
    #h = Hill(img,key)
    #encrypted_img = h.encrypt()
    #encrypted_img.save("im.jpg")

    #return html.Img


    
 # Vigenere

@app.callback(Output("cipher_vig","children"),
                Input("vig-c-b","n_clicks"),
                State("vig-c-t","value"),
                State("vig-c-k","value"))
def vig_enc(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    v = Vigenere(t,k)

    return v.encriptar()


@app.callback(Output("decrypt_vig","children"),
                Input("vig-d-b","n_clicks"),
                State("vig-d-t","value"),
                State("vig-d-k","value"))
def vig_dec(n,t,k):
    if ((not n) or (not t) or (not k)):
        raise dash.exceptions.PreventUpdate

    v = Vigenere(t,k)

    return v.desencriptar()


@app.callback(Output("cr_vig","children"),
                Input("vig-cr-b","n_clicks"),
                State("vig-cr","value"),)
def vig_cr(n,t):
    if ((not n) or (not t)):
        raise dash.exceptions.PreventUpdate

    v = Vigenere(t,"aaa")

    return v.criptoanalisis(30)



@app.callback(Output("af_vig","children"),
                Input("af-c-b","n_clicks"),
                State("af-c-t","value"),
                State("af-c-k1","value"),
                State("af-c-k2","value"))
def aff_enc(n,t,k1,k2):
    if ((not n) or (not t) or (not k1) or (not k2)):
        raise dash.exceptions.PreventUpdate

    a = Afin(t,k1,k2)

    return a.encriptar()



@app.callback(Output("decrypt_af","children"),
                Input("af-d-b","n_clicks"),
                State("af-d-t","value"),
                State("af-d-k1","value"),
                State("af-d-k2","value"))
def af_dec(n,t,k1,k2):
    if ((not n) or (not t) or (not k1) or (not k2)):
        raise dash.exceptions.PreventUpdate

    a = Afin(t,k1,k2)

    return a.desencriptar()



@app.callback(Output("cr_af","children"),
                Input("af-cr","n_clicks"),
                State("af-t-cr","value"))
def af_freq(n,t):
    if ((not n) or (not t)):
        raise dash.exceptions.PreventUpdate

    a = Afin(t,5,8)

    l = a.getLetterFrecuency()
    flat_list = [item for sublist in l for item in sublist]

    return flat_list



@app.callback(Output("cr_aff","children"),
                Input("afff-cr","n_clicks"),
                State("aff-cr","value"),
                State("aff-l1","value"),
                State("aff-l2","value"),
                State("aff-l3","value"),
                State("aff-l4","value"))
def af_crip(n,t,l1,l2,l3,l4):
    if ((not n) or (not t) or (not l1) or (not l2) or (not l3) or (not l4)):
        raise dash.exceptions.PreventUpdate

    a = Afin(t,5,8)

    l = a.criptoanalisis(l1,l2,l3,l4)


    return l












	
app.layout = html.Div([
    dcc.Tabs(id="cryptosystems", value = "tab-1", className="py-3", children=[

        dcc.Tab(label="Shift", children=[

            html.Div([html.H1("CIPHER"),
                       html.H2("Enter the text and key for cipher: "),
                       dcc.Input(id="t-shift-c",type="text",placeholder="Text"),
                       dcc.Input(id="k-shift-c", type="number",placeholder="Key"),
                       html.Button('Cipher',id="c-shift-c"),
                       html.Div(id="cipher_shift"),
                       html.Hr(),

                       html.H1("DECRYPTION"),
                       html.H2("Enter the text and key for decryption: "),
                       dcc.Input(id="t-shift-d",type="text",placeholder="Text"),
                       dcc.Input(id="k-shift-d", type="number",placeholder="Key"),
                       html.Button('Decrypt',id="c-shift-d"),
                       html.Div(id="decrypt_shift"),
                       html.Hr(),
                       
                       
                       html.H1("CRYPTANALYSIS"),
                       html.H2("Enter text for cryptanalysis: "),
                       dcc.Input(id="t-shift-cr",type="text",placeholder="Text"),
                       html.Button('CryptoAnalysis',id="shift-cr"),
                       html.Div(id="cr_shift"),
                       html.Hr(),                       ]

                       )


                                            ]),
        dcc.Tab(label="Substitution", children=[

                    html.H1("CIPHER"),
                    html.H2("Enter the text and key for cipher: "),
                    dcc.Input(id="subs-c-t",type="text",placeholder="Text"),
                    dcc.Input(id="subs-c-k", type="text",placeholder="Key"),
                    html.Button('Cipher',id="subs-c-b"),
                    html.Div(id="cipher_substitution"),
                    html.Hr(),

                    html.H1("DECRYPT"),
                    html.H2("Enter the text and key for decrypt: "),
                    dcc.Input(id="subs-d-t",type="text",placeholder="Text"),
                    dcc.Input(id="subs-d-k", type="text",placeholder="Key"),
                    html.Button('Decrypt',id="subs-d-b"),
                    html.Div(id="decrypt_subs"),
                    html.Hr(),


                                ]),

        dcc.Tab(label="Permutation", children=[
        
                    html.H1("CIPHER"),
                    html.H2("Enter the text and permutation for cipher: "),
                    dcc.Input(id="perm-c-t",type="text",placeholder="Text"),
                    dcc.Input(id="perm-c-k", type="text",placeholder="Permutation"),
                    html.Button('Cipher',id="perm-c-b"),
                    html.Div(id="cipher_perm"),
                    html.Hr(),

                    html.H1("DECRYPT"),
                    html.H2("Enter the text and permutation for decrypt: "),
                    dcc.Input(id="perm-d-t",type="text",placeholder="Text"),
                    dcc.Input(id="perm-d-k", type="text",placeholder="Permutation"),
                    html.Button('Decrypt',id="perm-d-b"),
                    html.Div(id="decrypt_perm"),
                    html.Hr(),


                    html.H1("CRYPTANALYSIS"),
                    html.H2("Enter the text for cryptanalysis: "),
                    dcc.Input(id="perm-cr-t",type="text",placeholder="Text"),
                    html.Button('Cryptanalysis',id="perm-cr-b"),
                    html.Div(id="cr_perm"),
                    html.Hr(),
        
        ]),
        dcc.Tab(label="Hill" , children=[

                   html.H1("CIPHER"),
                    html.H2("Enter the image and key for cipher: "),
                    dcc.Upload(id="up_img", children=html.Div(['Drag and Drop or', html.A('Select Files')])),
                    dcc.Input(id="hill-k-size", type="number",placeholder="key size"),
                    dcc.Input(id="hill-k", type="text",placeholder="Key"),
                    html.Button('Cipher',id="hill-c-b"),
                    html.Div(id="cipher_hill"),
                    html.Hr(),



        ]),
        dcc.Tab(label="Vigenere", children = [

                   html.H1("CIPHER"),
                    html.H2("Enter the text and key for cipher: "),
                    dcc.Input(id="vig-c-t",type="text", placeholder = "Text"),
                    dcc.Input(id="vig-c-k", type="text",placeholder="Key"),
                    html.Button('Cipher',id="vig-c-b"),
                    html.Div(id="cipher_vig"),
                    html.Hr(),

                   html.H1("Decrypt"),
                    html.H2("Enter the text and key for decrypt: "),
                    dcc.Input(id="vig-d-t",type="text", placeholder = "Text"),
                    dcc.Input(id="vig-d-k", type="text",placeholder="Key"),
                    html.Button('Decrypt',id="vig-d-b"),
                    html.Div(id="decrypt_vig"),
                    html.Hr(),

                       html.H1("CRYPTANALYSIS"),
                       html.H2("Enter text for cryptanalysis: "),
                       dcc.Input(id="vig-cr",type="text",placeholder="Text"),
                       html.Button('Cryptanalysis',id="vig-cr-b"),
                       html.Div(id="cr_vig"),
                       html.Hr(),         


        ]),
        dcc.Tab(label="Affin", children = [

                   html.H1("CIPHER"),
                    html.H2("Enter the text ,key and key for cipher: "),
                    dcc.Input(id="af-c-t",type="text", placeholder = "Text"),
                    dcc.Input(id="af-c-k1", type="number",placeholder="Key 1"),
                    dcc.Input(id="af-c-k2", type="number",placeholder="Key 2"),

                    html.Button('Cipher',id="af-c-b"),
                    html.Div(id="af_vig"),
                    html.Hr(),

                   html.H1("DECRYPT"),
                    html.H2("Enter the text and key for decrypt: "),
                    dcc.Input(id="af-d-t",type="text", placeholder = "Text"),
                    dcc.Input(id="af-d-k1", type="number",placeholder="Key 1"),
                    dcc.Input(id="af-d-k2", type="number",placeholder="Key 2"),
                    html.Button('Decrypt',id="af-d-b"),
                    html.Div(id="decrypt_af"),
                    html.Hr(),


                       html.H1("FREQUENCIES"),
                       html.H2("Enter text for cryptanalysis: "),
                       dcc.Input(id="af-t-cr",type="text",placeholder="Text"),
                       html.Button('frequencies',id="af-cr"),
                       html.Div(id="cr_af"),
                       html.Hr(),

                       html.H1("CRYPTANALYSIS"),
                       html.H2("Enter text for cryptanalysis: "),
                       dcc.Input(id="aff-cr",type="text",placeholder="Text"),
                       dcc.Input(id="aff-l1",type="text",placeholder="Letter 1"),
                       dcc.Input(id="aff-l2",type="text",placeholder="Letter 2"),
                       dcc.Input(id="aff-l3",type="text",placeholder="Letter 3"),
                       dcc.Input(id="aff-l4",type="text",placeholder="Letter 4"),
                       html.Button('CryptoAnalysis',id="afff-cr"),
                       html.Div(id="cr_aff"),
                       html.Hr(),    


        ])





    ])

])



if __name__ == '__main__':
    app.run_server(debug=True)