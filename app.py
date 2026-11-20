from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


def calcular_dias_restantes(data_atual):
    proximo_ano = data_atual.year + 1
    data_ano_novo = date(proximo_ano, 1, 1)

    dias_faltantes = data_ano_novo - data_atual
    return dias_faltantes.days


@app.route("/")
def pagina_inicial():
    data_corrente = date.today()

    dias_restantes = calcular_dias_restantes(data_corrente)
    # dias_restantes = 0

    return render_template(
        "index.html",
        dias_restantes=dias_restantes,
        ano_novo=data_corrente.year + 1,
        data_atual=data_corrente.strftime("%d/%m/%Y"),
    )


if __name__ == "__main__":
    app.run(debug=True)
