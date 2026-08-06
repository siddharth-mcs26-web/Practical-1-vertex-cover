#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using Edge = pair<int, int>;

void generateRandomGraph(int vertexCount, int edgeCount, vector<Edge>& edges) {
    if (vertexCount <= 0) {
        throw invalid_argument("Number of vertices must be positive.");
    }

    const int maxPossibleEdges = vertexCount * (vertexCount - 1) / 2;
    if (edgeCount < 0 || edgeCount > maxPossibleEdges) {
        throw invalid_argument("Number of edges is out of range for a simple graph.");
    }

    random_device seed;
    mt19937 generator(seed());
    uniform_int_distribution<int> distribution(0, vertexCount - 1);

    set<Edge> uniqueEdges;

    while (static_cast<int>(uniqueEdges.size()) < edgeCount) {
        int firstVertex = distribution(generator);
        int secondVertex = distribution(generator);

        if (firstVertex == secondVertex) {
            continue;
        }

        if (firstVertex > secondVertex) {
            swap(firstVertex, secondVertex);
        }

        uniqueEdges.insert({firstVertex, secondVertex});
    }

    edges.assign(uniqueEdges.begin(), uniqueEdges.end());
}

void printGraph(int vertexCount, const vector<Edge>& edges, ostream& out) {
    out << "Vertices: " << vertexCount << "\n";
    out << "Edges: " << edges.size() << "\n";

    for (const auto& [from, to] : edges) {
        out << from << " " << to << "\n";
    }
    out << "\n";
}

int main() {
    const int vertexCount = 10;
    const vector<int> edgeCounts = {10, 15, 20, 25, 30, 35, 40, 45};
    ofstream outputFile("graph_output.txt");

    if (!outputFile) {
        cerr << "Unable to create output file.\n";
        return 1;
    }

    cout << "Generating random graphs for different edge counts...\n";
    cout << "------------------------------------------------\n";

    for (int edgeCount : edgeCounts) {
        vector<Edge> edges;
        generateRandomGraph(vertexCount, edgeCount, edges);

        cout << "Graph with n = " << vertexCount << " and m = " << edgeCount << "\n";
        printGraph(vertexCount, edges, cout);

        outputFile << "Graph with n = " << vertexCount << " and m = " << edgeCount << "\n";
        printGraph(vertexCount, edges, outputFile);
    }

    outputFile.close();
    cout << "Output saved to graph_output.txt\n";

    return 0;
}
