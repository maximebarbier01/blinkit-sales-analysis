WITH base AS (
	SELECT 
		s1.order_id
		,s1.customer_id
		,s1.order_total
		,s1.payment_method
		,s1.delivery_partner_id
		,s1.store_id
		,s1.nb_orders_by_customer
		,s1.segment
		,s1.order_date
		,s2.order_date AS previous_order_date
		,(s1.order_date - s2.order_date) AS repurchase_duration
	FROM public.blinkit_segements AS s1
	JOIN public.blinkit_segements AS s2
		ON s1.customer_id = s2.customer_id AND s1.nb_orders_by_customer=s2.nb_orders_by_customer+1
	ORDER BY 
		customer_id
		,nb_orders_by_customer
)
-- Temps entre 2 commandes -- 
SELECT 
	payment_method
	,ROUND(AVG(repurchase_duration)/31,2) AS avg_repurchase_duration
	,COUNT(customer_id) AS nb_customers
FROM base
GROUP BY payment_method
-- Résultats - par segment : frequent : 3 mois / occasional : 5 mois 
-- Résultats - payment_method : 4,7 mois pour tous les moyens de paiement environ 

	