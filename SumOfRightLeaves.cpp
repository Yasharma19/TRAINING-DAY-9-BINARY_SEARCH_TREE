#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

// Binary Tree Node
struct Node {
    int value;
    Node* left;
    Node* right;
};

// Function to create a new node
Node* createNode(int value) {
    Node* newNode = new Node();
    if (newNode) {
        newNode->value = value;
        newNode->left = newNode->right = nullptr;
    }
    return newNode;
}

// Function to insert a node into the binary search tree
Node* insertNode(Node* root, int value) {
    if (root == nullptr) {
        root = createNode(value);
        return root;
    }

    if (value < root->value) {
        root->left = insertNode(root->left, value);
    } else if (value > root->value) {
        root->right = insertNode(root->right, value);
    }

    return root;
}

// Function to calculate the sum of all right leaves in the binary search tree
int sumOfRightLeaves(Node* root) {
    if (root == nullptr)
        return 0;

    int sum = 0;

    if (root->right != nullptr && root->right->left == nullptr && root->right->right == nullptr)
        sum += root->right->value;

    sum += sumOfRightLeaves(root->left) + sumOfRightLeaves(root->right);

    return sum;
}

int main() {
    int n;
    cin >> n;

    Node* root = nullptr;

    int value;
    for (int i = 0; i < n; i++) {
        cin >> value;
        root = insertNode(root, value);
    }

    int sum = sumOfRightLeaves(root);
    cout << sum << endl;

    return 0;
}