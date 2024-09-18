lua_estelar = int(input())
essencia_dragao = int(input())
lagrimas_fenix = int(input())

preco_lua = 5
preco_essencia = 3
preco_lagrimas = 8
if lua_estelar and essencia_dragao and lagrimas_fenix == 0:
    print('')
else:
    custo_total = (lua_estelar * preco_lua) + (essencia_dragao * preco_essencia) + (lagrimas_fenix * preco_lagrimas)
    print(custo_total)


