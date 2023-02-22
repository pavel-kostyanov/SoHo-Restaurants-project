class Node
{
    private:
        int value;
        int next_node;

    public:

        Node(int val, int nextNode) : value(val), next_node(nextNode)
        {   }

        void set_next_node(int nextNode)
        {
            next_node = nextNode;
        }

        int get_next_node()
        {
            return next_node;
        }

        int get_value()
        {
            return value;
        }
};
