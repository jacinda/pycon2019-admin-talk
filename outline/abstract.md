### Introduction / Things the admin does well (3 min)

	* Opening: This talk is all demonstration based.  There are very few slides, which I hope you approve of, even though we all know I'm tempting the presentation gods here.
	* How many of you love all the good things the admin does for you? Isn't it a great feeling to add a couple lines of code and automatically have a GUI to interact with your database?  It feels blazingly fast, and your development races along. You're concentrating on building out features and out-pacing your competitors and this gives you a tremendous advantage as a developer and company. Your usage explodes and your database grows. As you add new features, your model relationships begin to get more complex and you have more joins. You've modified what the admin displays in order to give your admin users the ability to see more information at once. Sounds perfect, right?  Until one day...people start asking you why this page is taking longer and longer to load...and then you start seeing more load on your database...now you're thinking about whether you need to build out a custom admin interface and thinking about how that's going to take time away from your primary goals.
	* But wait!  You've come to the right place. While there may be times where a custom interface is the way to go, there are other times where with a few tweaks you can improve your performance directly in the admin.
	

* Makes development very fast
* For many use cases, it "does the right thing" automatically.  For example, modifying the HTML in a callable won't cause new queries.

### display of basic django-debug-toolbar usage

	* Now, before we get into the details, I'm going to take a brief detour to demonstrate django-debug-toolbar. For the veterans in the audience, this will probably seem old hat, but for any beginners this is a tool that you should learn to love.
	* Walk through setup 


### What can sneak up on you (5 min)

* Having lots of related items visible in the list view
* Using list_select_related
* Overriding queryset for additional select_related and prefetch_related options

### What to avoid in callables (3 min)

* Queries that will be executed on every row

### The default widgets for many-to-many and foreign key fields (3 min)

* What widgets to use to replace the defaults based on how many options you have in your database

### Custom aggregates in the list view (i.e. custom querysets) (3 min)

* When this is a good idea
* When this is too slow and you need other options

### More general performance improvements through caching (3-5 min)

* Django's caching framework
* Caching with third-party packages / tools
* Custom caching with Redis

### Questions (Remaining time)