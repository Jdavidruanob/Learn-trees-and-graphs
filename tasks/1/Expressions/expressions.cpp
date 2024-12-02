/*

Jose David Ruano Burbano
Tarea 1 - Expressions
Arboles y grafos 2024-2

Análisis de complejidad:

La complejidad temporal del algoritmo se puede dividir en dos partes principales: la construcción del árbol y el recorrido por niveles.

1. ConstructTree:
constructTree recorre cada carácter de la cadena de entrada una vez. Para cada carácter, realiza operaciones de inserción y eliminación en 
la pila, que son operaciones O(1). Eso quiere decir que la complejidad es O(n), donde n es la longitud de la cadena de entrada.

2. LevelOrder:
levelOrder realiza un recorrido por niveles del árbol, por ende en el peor de los casos, visita cada nodo del árbol una vez.
La inserción y eliminación en la cola son operaciones O(1). Sin embargo, la operación `ans.insert(ans.begin(), node->value);` tiene una complejidad de O(k) en el peor de los casos, donde k es la longitud actual de la cadena. Dado que esta operación se realiza para cada nodo, la complejidad total de esta parte es O(m^2), donde m es el número de nodos en el árbol.

Así, tendríamos que la complejidad temporal total del algoritmo es O(n + m^2). En el caso promedio, n y m son equivalentes, por lo que la complejidad puede ser aproximada a O(n^2).

*/
#include <iostream>
#include <string>
#include <stack>
#include <queue>

using namespace std;

class TreeNode {
public:
    char value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(char value) {
        this->value = value;
        left = nullptr;
        right = nullptr;
    }
};

class ExpressionTree {
private:
    TreeNode* root;

    TreeNode* constructTree(const string& line) {
        stack<TreeNode*> st;
        for (char letter : line) {
            if (islower(letter)) {
                st.push(new TreeNode(letter));
            } else {
                TreeNode* node = new TreeNode(letter);
                TreeNode* right = st.top(); st.pop();
                TreeNode* left = st.top(); st.pop();
                node->left = left;
                node->right = right;
                st.push(node);
            }
        }
        return st.top();
    }

    string levelOrder(TreeNode* root) {
        string ans;
        if (!root) {
            return ans;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            ans.insert(ans.begin(), node->value);

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }

        return ans;
    }

public:
    ExpressionTree(const string& expression) {
        root = constructTree(expression);
    }

    string getLevelOrder() {
        return levelOrder(root);
    }
};

int main() {
    int T;
    cin >> T;
    while (T--) {
        string line;
        cin >> line;
        ExpressionTree tree(line);
        string transformedExpression = tree.getLevelOrder();
        cout << transformedExpression << endl;
    }
    return 0;
}

