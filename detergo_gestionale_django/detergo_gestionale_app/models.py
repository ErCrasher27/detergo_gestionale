from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=64)
    cognome = models.CharField(max_length=64)
    telefono = models.CharField(max_length=16, null=True)
    indirizzo = models.CharField(max_length=128, null=True)
    note = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"


class Ordine(models.Model):
    stato = [
        ('NO', 'non_iniziato'),
        ('PA', 'pariziale'),
        ('CO', 'completato')
    ]
    data_attuale = models.DateTimeField(auto_now=True)
    data_ritiro = models.DateField()
    totale = models.FloatField()
    credito = models.FloatField()
    domicilio = models.BooleanField()
    stato = models.CharField(max_length=2, choices=stato)
    note = models.CharField(max_length=256)
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='get_cliente')

    def __str__(self):
        return self.data_attuale

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"


class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    icona = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"


class Articolo(models.Model):
    nome = models.CharField(max_length=64)
    prezzo_acqua = models.FloatField()
    prezzo_secco = models.FloatField()
    prezzo_sartoria = models.FloatField()
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='get_categoria')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"


class Colore(models.Model):
    nome = models.CharField(max_length=64)
    icona = models.CharField(max_length=256)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Colore"
        verbose_name_plural = "Colori"


class Difetto(models.Model):
    nome = models.CharField(max_length=64)
    icona = models.CharField(max_length=256)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Difetto"
        verbose_name_plural = "Difetti"
        

class CapoPortato(models.Model):
    stato = [
        ('NO', 'non_iniziato'),
        ('PA', 'pariziale'),
        ('CO', 'completato')
    ]
    stato = models.CharField(max_length=2, choices=stato)
    prezzo_modificato = models.FloatField(null=True)
    foto = models.CharField(max_length=256, null=True)
    id_ordine = models.ForeignKey(
        Ordine, on_delete=models.CASCADE, related_name='get_ordine')
    id_articolo = models.ForeignKey(
        Articolo, on_delete=models.CASCADE, related_name='get_articolo')
    colore = models.ManyToManyField(Colore)
    difetto = models.ManyToManyField(Difetto)

    def __str__(self):
        return self.id_ordine + " " + self.id_articolo

    class Meta:
        verbose_name = "CapoPortato"
        verbose_name_plural = "CapiPortati"