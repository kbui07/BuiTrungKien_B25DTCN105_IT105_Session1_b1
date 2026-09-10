def display_revenue_report(raw_orders):
    total_revenue = 0
    successful_orders = 0

    print("=== MÀN HÌNH BÁO CÁO DOANH THU GIAO HÀNG ===")

    for order in raw_orders:
        if order["status"] == "DELIVERED":
            total_revenue += order["fee"]
            successful_orders += 1

    if successful_orders > 0:
        average_revenue = total_revenue / successful_orders
    else:
        average_revenue = 0

    print("Tổng doanh thu:", total_revenue, "đ")
    print("Số đơn thành công:", successful_orders)
    print("Doanh thu trung bình:", average_revenue, "đ")


order_data = [
    {"order_id": "01", "fee": 15000, "status": "DELIVERED"},
    {"order_id": "02", "fee": 20000, "status": "DELIVERED"},
    {"order_id": "03", "fee": 0, "status": "CANCELLED"},
    {"order_id": "04", "fee": -5000, "status": "RETURNED"},
    {"order_id": "05", "fee": 25000, "status": "DELIVERED"}
]

display_revenue_report(order_data)