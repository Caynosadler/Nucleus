import aiml
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)

Alex = aiml.Kernel()
Alex.learn('bornin.aiml')
Alex.learn('calendar.aiml')
Alex.learn('chatbots32.aiml')
Alex.learn('currency.aiml')
Alex.learn('default.aiml')
Alex.learn('horoscope.aiml')
Alex.learn('howmany.aiml')
Alex.learn('jokes.aiml')
Alex.learn('learn.aiml')
Alex.learn('maths.aiml')
Alex.learn('shutup.aiml')
Alex.learn('stack.aiml')
Alex.learn('warnings.aiml')
Alex.learn('whatday_eng.aiml')
Alex.learn('whatday_usa.aiml')
Alex.learn('yomama.aiml')
#Alex.learn('standard/startup.xml')
Alex.learn('ai.aiml')
Alex.learn('inquiry.aiml')
Alex.learn('phone.aiml')
Alex.learn('religion.aiml')
Alex.learn('astrology.aiml')
#Alex.learn('ava/atomic.aiml')
Alex.learn('bot.aiml')
Alex.learn('client_profile.aiml')
Alex.learn('computers.aiml')
Alex.learn('history.aiml')
Alex.learn('money.aiml')
Alex.learn('loebner10.aiml')
Alex.learn('mp6.aiml')
Alex.learn('drugs.aiml')
Alex.learn('continuation.aiml')
Alex.learn('date.aiml')
Alex.learn('movies.aiml')
Alex.learn('humor.aiml')
Alex.learn('numbers.aiml')
Alex.learn('mp0.aiml')
Alex.learn('personality.aiml')
Alex.learn('psychology.aiml')
Alex.learn('imponderables.aiml')
Alex.learn('reduction.names.aiml')
Alex.learn('reduction0.safe.aiml')
Alex.learn('salutations.aiml')
Alex.learn('science.aiml')
Alex.learn('sex.aiml')
Alex.learn('update1.aiml')
Alex.learn('update_mccormick.aiml')
Alex.learn('wallace.aiml')
Alex.learn('xfind.aiml')
Alex.learn('sports.aiml')
Alex.learn('stack.aiml')
Alex.learn('reduction2.safe.aiml')
Alex.learn('pickup.aiml')
Alex.learn('mp2.aiml')
Alex.learn('interjection.aiml')
Alex.learn('iu.aiml')
Alex.learn('startup.aiml')
Alex.learn('mp3.aiml')
Alex.learn('politics.aiml')
Alex.learn('knowledge.aiml')
Alex.learn('mp4.aiml')
Alex.learn('stories.aiml')
Alex.learn('literature.aiml')
Alex.learn('mp5.aiml')
Alex.learn('primitive-math.aiml')
Alex.learn('that.aiml')
Alex.learn('reduction3.safe.aiml')
Alex.learn('reduction4.safe.aiml')
Alex.learn('reductions-update.aiml')
Alex.learn('drugs.aiml')
Alex.learn('biography.aiml')
Alex.learn('bot.aiml')
Alex.learn('bot_profile.aiml')
Alex.learn('food.aiml')
Alex.learn('client.aiml')
Alex.learn('geography.aiml')
Alex.learn('gossip.aiml')

@app.route('/<question>')
def ask(question):
    response = Alex.respond(question)
    return response

if __name__=='__main__':
    app.run(debug=True, port=8000)
