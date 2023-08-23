# Copyright (c) 2023 kk
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# pdm init
# pdm add errbot
# pdm add errbot-backend-slackv3
# pdm run start
# pdm update
# pdm -v export --without-hashes >requirements.txt

require 'rake'
require 'erb'
require 'time'

task default: %w[push]

task :push do
  Rake::Task['fmt'].invoke
  sh "git add . && \
      git commit -m 'Update #{Time.now}.' && \
      git push origin main
    "
end

task :new do
  $stdout.print 'plugin name: '
  @name = $stdin.gets.strip
  Dir.mkdir "plugins/err-#{@name}"

  File.open("plugins/err-#{@name}/README.md", 'w') do |f|
    f.write "# #{@name}\n\n#{@name}"
  end

  File.open("plugins/err-#{@name}/#{@name}.py", 'w') do |f|
    f.write(ERB.new(File.open('templates/plugin.py.erb', 'r').read).result(binding))
    puts "plugins/err-#{@name}/#{@name}.py created."
  end

  File.open("plugins/err-#{@name}/#{@name}.plug", 'w') do |f|
    f.write(ERB.new(File.open('templates/plugin.plug.erb', 'r').read).result(binding))
    puts "plugins/err-#{@name}/#{@name}.plug created."
  end
end

# errbot only supports python 3.6.x
# task :run do
#   sh 'pdm run start'
# end

task :run do
  sh 'errbot'
end

task :fmt do
  # sh 'pdm run python -m black .'
  sh 'python -m black .'
end
