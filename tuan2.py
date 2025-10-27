class Node:
    """Lớp Node đại diện cho một nút trong cây BST"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Lớp Cây nhị phân tìm kiếm (BST)"""
    def __init__(self):
        self.root = None
    
    # Thêm giá trị vào BST
    def insert(self, key):
        """Thêm một giá trị vào BST"""
        if self.root is None:
            self.root = Node(key)
        else: 
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """Hàm đệ quy để thêm nút"""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
    
    # Tìm kiếm giá trị trong BST
    def search(self, key):
        """Tìm kiếm một giá trị trong BST"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Hàm đệ quy để tìm kiếm"""
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    # Xóa giá trị khỏi BST
    def delete(self, key):
        """Xóa một giá trị khỏi BST"""
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        """Hàm đệ quy để xóa nút"""
        if node is None:
            return node
        
        # Tìm nút cần xóa
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Tìm thấy nút cần xóa
            # Trường hợp 1: Nút lá hoặc có 1 con
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Trường hợp 2: Nút có 2 con
            # Tìm nút kế nhiệm (nút nhỏ nhất bên phải)
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)
        
        return node
    
    def _find_min(self, node):
        """Tìm nút có giá trị nhỏ nhất trong cây con"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # Duyệt cây BST
    
    def inorder(self):
        """Duyệt In-order (Trái - Gốc - Phải)
        Kết quả: Các phần tử theo thứ tự tăng dần"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        """Duyệt Pre-order (Gốc - Trái - Phải)
        Kết quả: Gốc được duyệt trước"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        """Duyệt Post-order (Trái - Phải - Gốc)
        Kết quả: Gốc được duyệt sau cùng"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)
    
    def levelorder(self):
        """Duyệt Level-order (Theo từng mức/tầng)
        Sử dụng hàng đợi (queue) - BFS"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    # Phần thông tin cây
    
    def is_empty(self):
        """Kiểm tra cây có rỗng không"""
        return self.root is None
    
    def get_height(self):
        """Tính chiều cao của cây"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                      self._height_recursive(node.right))
    
    def display_tree(self, node=None, level=0, prefix="Root: "):
        """Hiển thị cây dạng text (nằm ngang)"""
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                if node.left:
                    self.display_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                
                if node.right:
                    self.display_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# Chương trình chính để demo các chức năng của BST
if __name__ == "__main__":
    # Tạo cây BST
    bst = BinarySearchTree()
    
    print("=" * 50)
    print("DEMO CÂY NHỊ PHÂN TÌM KIẾM (BST)")
    print("=" * 50)
    
    elements = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    print(f"\n1. THÊM CÁC PHẦN TỬ: {elements}")
    for elem in elements:
        bst.insert(elem)
    
    print("\n2. CẤU TRÚC CÂY:")
    bst.display_tree()
    
    # 4 phép duyệt
    print(f"\n3. CÁC PHÉP DUYỆT CÂY:")
    print(f"   In-order   (LNR): {bst.inorder()}")
    print(f"   Pre-order  (NLR): {bst.preorder()}")
    print(f"   Post-order (LRN): {bst.postorder()}")
    print(f"   Level-order (BFS): {bst.levelorder()}")
    
    # Tìm kiếm
    print(f"\n4. TÌM KIẾM:")
    search_keys = [40, 100]
    for key in search_keys:
        found = bst.search(key)
        print(f"   Tìm {key}: {'Có' if found else 'Không có'}")
    
    # Xóa phần tử
    print(f"\n5. XÓA PHẦN TỬ:")
    delete_keys = [20, 30, 50]
    for key in delete_keys:
        print(f"\n   Xóa {key}:")
        bst.delete(key)
        print(f"   In-order sau khi xóa: {bst.inorder()}")
    
    # Thông tin cây
    print(f"\n6. THÔNG TIN CÂY:")
    print(f"   Chiều cao cây: {bst.get_height()}")
    print(f"   Cây rỗng? {'Có' if bst.is_empty() else 'Không'}")
    
    print("\n" + "=" * 50)
    print("CẤU TRÚC CÂY SAU CÁC THAO TÁC:")
    print("=" * 50)
    bst.display_tree()
