---
name: architecture-systems
description: Master system design and scalable architecture. Learn distributed systems, scalability patterns, high availability, and designing large-scale systems.
---

# System Design & Architecture

## Scalability Concepts

### Vertical Scaling
```
Single powerful server
Cheaper initially
Limited growth
Hardware limits
```

### Horizontal Scaling
```
Multiple servers
Load balancing
Redundancy
Unlimited growth
```

## Caching Strategies

### Cache Levels
```
1. Client-side caching
2. CDN caching
3. Application caching (Redis)
4. Database query caching
5. Database replication
```

### Cache Invalidation
```
1. TTL (Time-To-Live)
2. LRU (Least Recently Used)
3. Event-based invalidation
4. Manual invalidation
```

## Database Scaling

### Vertical Scaling
```
Upgrade hardware
Indexes
Query optimization
Connection pooling
```

### Horizontal Scaling
```
Replication (Master-Slave)
Sharding (by hash/range/directory)
Partitioning
Read replicas
```

## Distributed Systems

### CAP Theorem
```
C - Consistency (all nodes same data)
A - Availability (system always responsive)
P - Partition tolerance (network failures)

Choose 2 of 3
- Consistent & Available (single region)
- Consistent & Partition-tolerant (wait for sync)
- Available & Partition-tolerant (eventual consistency)
```

### Consensus Algorithms
```
- Paxos: Strong consistency
- Raft: Easier to understand Paxos
- CRDT: Eventual consistency
```

## API Gateway Pattern
```
Client → API Gateway → Services
          ├─ Load Balancing
          ├─ Authentication
          ├─ Rate Limiting
          ├─ Request Routing
```

## Microservices Architecture
```
Monolith → Services by Domain
├─ User Service
├─ Order Service
├─ Payment Service
└─ Notification Service
```

## High Availability
```
✅ Redundancy
✅ Load Balancing
✅ Failover
✅ Health Checks
✅ Auto-scaling
✅ Disaster Recovery
✅ Multi-region
```

## Messaging & Queues
```
Synchronous: REST, gRPC (immediate)
Asynchronous: Message Queue (eventual)

Benefits:
- Decoupling services
- Retry logic
- Load shifting
- Order processing
```

## Monitoring & Observability
```
Metrics: Prometheus
Logs: ELK Stack
Traces: Jaeger
Dashboards: Grafana
Alerts: Custom rules
```

## Key Metrics

✅ Latency (response time)
✅ Throughput (requests/sec)
✅ Error rate
✅ Availability (uptime %)
✅ Scalability (growth capacity)
✅ Cost efficiency

