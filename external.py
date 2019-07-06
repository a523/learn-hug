import hug
import internal


# 方法一：
# router = hug.route.API(__name__)
# router.get('/home')(internal.root)

# 方法二：
api = hug.API(__name__)
hug.get('/home', api=api)(internal.root)