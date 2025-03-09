# Cypher MATCH clause cheatsheet


## Table Returns

```cypher
// Customer orders
MATCH (c:Customer)-[p:PURCHASED]->(o:Order)
RETURN c.companyName, COUNT(o) as order_count;

// Product details with supplier
MATCH (p:Product)<-[:SUPPLIES]-(s:Supplier)
RETURN p.productName, p.unitPrice, s.companyName;

// Order details with products
MATCH (o:Order)-[:ORDERS]->(p:Product)
RETURN o.orderID, COLLECT(p.productName) as products, SUM(p.unitPrice) as total;
```

## Graph Path Returns

```cypher
// Customer order chain
MATCH path = (c:Customer)-[:PURCHASED]->(o:Order)-[:ORDERS]->(p:Product)
RETURN path limit 100;

// Supply chain visualization
MATCH path = (s:Supplier)-[:SUPPLIES]->(p:Product)<-[:ORDERS]-(o:Order)
RETURN path  limit 100;

// Customer-Employee interactions
MATCH path = (c:Customer)-[:PURCHASED]->(o:Order)<-[:SOLD]-(e:Employee)
RETURN path  limit 100;
```

# Cypher Filtering Patterns

## Numeric Filters

```cypher
// Price range
MATCH (p:Product)
WHERE 20 <= p.unitPrice <= 50
RETURN p.productName, p.unitPrice;

// Quantity thresholds
MATCH (o:Order)-[rel:ORDERS]->(p:Product)
WHERE rel.quantity > 100
RETURN o.orderID, p.productName, rel.quantity;
```

## String Filters
```cypher
// Starts with
MATCH (c:Customer)
WHERE c.companyName STARTS WITH 'A'
RETURN c.companyName;

// Contains
MATCH (p:Product)
WHERE p.productName CONTAINS 'Cheese'
RETURN p.productName;

// Regular expression
MATCH (p:Product)
WHERE p.productName =~ '.*Sauce.*'
RETURN p.productName;
```

## Date Filters

```cypher
// Orders in 1997
MATCH (o:Order)
WHERE o.orderDate.year = 1997
RETURN o.orderID, o.orderDate;

// Last quarter
MATCH (o:Order)
WHERE o.orderDate >= date('1997-10-01')
  AND o.orderDate <= date('1997-12-31')
RETURN o.orderID;
```

## Multiple Conditions

```cypher
// Complex business rule
MATCH (c:Customer)-[:PURCHASED]->(o:Order)-[ord:ORDERS]->(p:Product)
WHERE p.unitPrice > 50
  AND ord.quantity >= 10
  AND c.country = 'Germany'
RETURN c.companyName, p.productName, ord.quantity;

// Using OR
MATCH (p:Product)
WHERE p.unitsInStock = 0
  OR p.discontinued = true
RETURN p.productName;
```

## Collection Filters

```cypher
// Using IN
MATCH (c:Customer)
WHERE c.country IN ['France', 'Germany', 'Spain']
RETURN c.companyName, c.country;

// List comprehension
MATCH (s:Supplier)-[:SUPPLIES]->(p:Product)
WHERE ALL(x IN p.unitPrice WHERE x < 100)
RETURN s.companyName;
```

## NULL Handling

```cypher
// Missing region
MATCH (c:Customer)
WHERE c.region IS NULL
RETURN c.companyName;

// Coalesce example
MATCH (c:Customer)
RETURN c.companyName,
       COALESCE(c.region, 'Unknown') as region;
```
