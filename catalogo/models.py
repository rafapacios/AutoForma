from django.db import models

class prodCad(models.Model):

    id = models.AutoField(primary_key=True)
    marca = models.CharField(verbose_name="Marca", max_length=50, blank=True)
    cod_fab = models.CharField(verbose_name="SKU Fabricante", max_length=100, blank=True)
    cod_int = models.CharField(verbose_name=r"Código Interno", max_length=200, blank=True)
    cat = models.CharField(verbose_name="Categorias", max_length=100, blank=True)
    modelo = models.CharField(verbose_name="Modelo", max_length=500, blank=True)
    desc = models.CharField(verbose_name="Descrição", max_length=1000, blank=True)
    preco = models.CharField(verbose_name=r"Preço", max_length=200, blank=True)
    cor = models.CharField(verbose_name=r"Cor da Página", max_length=100, blank=True)
    marcabusca = models.CharField(verbose_name="Marca interna", max_length=50, blank=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.marca
