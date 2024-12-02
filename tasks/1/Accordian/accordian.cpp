/*

Jose David Ruano Burbano
Tarea 1 - Accordian
Arboles y grafos 2024-2

Análisis de complejidad:
La complejidad temporal de este algoritmo es O(cantidad de cartas^2), donde esta cantidad es el numero de cartas en el deck.
Esto se debe a que en el peor de los casos, el algoritmo recorre todas las cartas en el deck y realiza comparaciones y combinaciones entre ellas,
la complejidad de las operaciones de combinación de pilas es O(cantidad de cartas^2) en el peor de los casos,
ya que cada carta puede ser comparada con otras cartas en el deck.
Por lo tanto, la complejidad temporal total es O(cantidad de cartas^2) o lo que es lo mismo en este caso O(52^2). 

*/


#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>

using namespace std;

int main() {
    string line;
    vector<stack<string>> deck;
    const int CARDS_DECK = 52;
    int flag = 1;
    while (getline(cin, line) && flag == 1) {
        if (line[0] == '#'){
            flag = 0;
            
        }; // Termina si encuentra #

        // Usar stringstream para dividir la línea en substrings
        stringstream ss(line);
        string card;
        while (ss >> card) {
            stack<string> pileOfcard;
            pileOfcard.push(card);
            deck.push_back(pileOfcard);

            if (deck.size() == CARDS_DECK) {
                int i = 0;
                // Se inicia a jugar accordian
                while (i < deck.size()) {
                    if (i > 2 && (deck[i].top()[0] == deck[i - 3].top()[0] || deck[i].top()[1] == deck[i - 3].top()[1])) {
                        deck[i - 3].push(deck[i].top());
                        deck[i].pop();
                        if (deck[i].empty()) {  // Si una pila se quedo sin cartas ya no nos sirve
                            deck.erase(deck.begin() + i);
                        }
                        i -= 4;
                    }
                    if (i > 0 && (deck[i].top()[0] == deck[i - 1].top()[0] || deck[i].top()[1] == deck[i - 1].top()[1])) {
                        deck[i - 1].push(deck[i].top());
                        deck[i].pop();
                        if (deck[i].empty()) {
                            deck.erase(deck.begin() + i);
                        }
                        i -= 2; 
                    }
                    i++;
                }

                // Imprimir la salida
                if (deck.size() == 1) {
                    cout << deck.size() << " pile" << " remaining:" ;
                } else {
                    cout << deck.size() << " piles" << " remaining:" ;
                }
                for (int i = 0; i < deck.size(); i++) {
                    cout << " " << deck[i].size();
                }
                cout << endl;
                
                deck.clear(); // Limpiar el deck para la siguiente ronda
            }
        }
    }

    return 0;
}