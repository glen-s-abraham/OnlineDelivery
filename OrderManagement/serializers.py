from rest_framework import serializers
from OrderManagement.models import Order,OrderedProduct

class OrderedProductSerializer(serializers.ModelSerializer):
	"""Model serializer for ordered product model"""
	
	class Meta:

		model=OrderedProduct
		fields=('id','product','qty','price')
	


class OrderSerializer(serializers.ModelSerializer):
	"""Order serializer"""
	orders=OrderedProductSerializer(many=True)
	class Meta:
		model=Order
		fields=('id','total_amount','status','orders')
	
	def create(self,validated_data):
		order_data = validated_data.pop('orders')
		newOrder = Order(**validated_data)
		newOrder.user=self.context['request'].user
		newOrder.save()
		for order in order_data:
			OrderedProduct.objects.create(order=newOrder,**order)
		return newOrder		
	def update(self,instance,validated_data):
		order_data = validated_data.pop('orders') 
		orders=(instance.orders).all()
		orders=list(orders)
		instance.total_amount=validated_data.get('total_amount', instance.total_amount)
		for order in order_data:
			print(order)
			o=orders.pop(0)
			o.product=order.get('product',o.product)
			o.price=order.get('price',o.price)
			o.qty=order.get('qty',o.qty)
			o.save()
		instance.save()	
		return instance	


		
       
        
"""
{
    "id": 19,
    "total_amount": "100.00",
    "status": "pl",
    "orders": [
        {
            "id": 4,
            "product": 1,
            "qty": "2.00",
            "price": "200.00"
        },
        {
            "id": 5,
            "product": 2,
            "qty": "2.00",
            "price": "200.00"
        },
        {
            "id": 6,
            "product": 3,
            "qty": "2.00",
            "price": "200.00"
        }
    ]
}        
"""           
      
		

		



		

