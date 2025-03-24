import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    # def _handleLingua(self):
    #     lingua = self._view._lingua.value
    #
    #     if lingua is None:
    #         self._view._txtOut.controls.append(ft.Text("Attenzione. Selezionare una lingua", color = "red"))
    #         self._view.page.update()
    #     else:
    #         self._view._txtOut.controls.append(ft.Text("Lingua selezionata", color = "green"))
    #         self._view.page.update()

    def _handleSpellCheck(self, e):
        lingua = self._view._lingua.value

        if lingua is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione. Selezionare una lingua", color="red"))
            self._view.page.update()
            return



        metodo = self._view._tipoRicerca.value
        if metodo is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione. Selezionare una tipologia di ricerca", color="red"))
            self._view.page.update()
            return



        testo = self._view._txtTesto.value
        if testo == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione. Inserire un contenuto", color="red"))
            self._view.page.update()
            return

        risultato = self.handleSentence(testo, lingua, metodo)
        self._view._txtFinale.controls.append(ft.Text(f"{testo}\nParole errate: {risultato[0]}\nTempo richiesto: {risultato[1]}\n"))


        self._view.page.update()





def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text